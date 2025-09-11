# message_frequency_counter.py
# Python 3.13 — frequency from per-message header.stamp only (sensor time)
# Keep all comments in English only.

import sys, gzip, random, re
from utilityx.os.path import Path
from typing import List, TextIO

class MessageFrequencyCounter:
    """
    This class can be used to find the frequency of sensors. since sensors are messages in ROS so generally it can find thethe frequency of ROS messages
    """
    def __init__(self, path:Path, topics:List[str], reservoir_k):
        """

        Args:
            path:
            topics: [
                    "/uav2/odometry/odom_gps",
                    "/uav2/rplidar/scan",
            ]
        """
        self._native_abs_path = path.get_native_absolute_path()
        self._topics = topics

        # Robust topic line: optional spaces, optional leading '#', optional quotes
        self._topic_reqular_expression = re.compile(r'^\s*(?:#\s*)?topic:\s*"?([^"\n]+)"?\s*$')

        # sample size for dt stability stats
        self._reservoir_k= reservoir_k

        #lazy loading
        self._stats = None


    def _open_text(self)-> TextIO:
        """

        Args:
            path:

        Returns:

        """
        if self._native_abs_path.endswith(".gz"):
            return gzip.open(path, "rt", encoding="utf-8", errors="ignore")
        return open(self._native_abs_path, "r", encoding="utf-8", errors="ignore")


    def _parse_header_stamps(self, fp, targets: set[str]):
        """
        Stream parse: yield (topic, ts) using ONLY header.stamp (secs+nsecs) once per message.
        Ignores any '# timestamp (sec): ...' lines entirely.
        """
        curr = None
        emitted_ts = False
        in_header = False
        in_stamp = False
        have_secs = have_nsecs = False
        secs = nsecs = 0

        for raw in fp:
            line = raw.rstrip("\n")

            # Start of a new message: match topic line robustly
            m = self._topic_reqular_expression.match(line)
            if m:
                topic = m.group(1).strip()
                curr = topic if topic in targets else None
                # reset per-message state
                emitted_ts = False
                in_header = False
                in_stamp = False
                have_secs = have_nsecs = False
                continue

            if curr is None:
                continue  # not a topic we care about

            ls = line.strip()

            # Enter header block
            if ls == "header:":
                in_header = True
                in_stamp = False
                have_secs = have_nsecs = False
                secs = nsecs = 0
                continue

            if in_header:
                # Enter stamp block inside header
                if ls == "stamp:":
                    in_stamp = True
                    have_secs = have_nsecs = False
                    secs = nsecs = 0
                    continue

                if in_stamp:
                    if ls.startswith("secs:"):
                        try:
                            secs = int(ls.split(":", 1)[1]);
                            have_secs = True
                        except ValueError:
                            pass
                    elif ls.startswith("nsecs:"):
                        try:
                            nsecs = int(ls.split(":", 1)[1]);
                            have_nsecs = True
                        except ValueError:
                            pass

                    # Emit exactly once per message
                    if have_secs and have_nsecs and not emitted_ts:
                        ts = float(secs) + float(nsecs) * 1e-9
                        yield curr, ts
                        emitted_ts = True
                        in_stamp = False
            # Everything else ignored


    def get_stats(self):
        if self._stats is None:
            targets = set(self._topics)
            stats: dict[str, dict] = {}
            with self._open_text() as fp:
                for topic, ts in self._parse_header_stamps(fp, targets):
                    s = stats.get(topic)
                    if s is None:
                        s = {
                            "count": 0,
                            "min_ts": ts,
                            "max_ts": ts,
                            "prev": None,
                            "good": 0,  # dt > 0
                            "neg_or_zero": 0,  # dt <= 0
                            "mindt": float("inf"),
                            "maxdt": 0.0,
                            "seen": 0,
                            "k": 0,
                            "sample": [],
                        }
                        stats[topic] = s

                    s["count"] += 1
                    if ts < s["min_ts"]: s["min_ts"] = ts
                    if ts > s["max_ts"]: s["max_ts"] = ts

                    if s["prev"] is not None:
                        dt = ts - s["prev"]
                        if dt > 0:
                            s["good"] += 1
                            if dt < s["mindt"]: s["mindt"] = dt
                            if dt > s["maxdt"]: s["maxdt"] = dt
                            s["seen"] += 1
                            if s["k"] < self._reservoir_k:
                                s["sample"].append(dt);
                                s["k"] += 1
                            else:
                                j = random.randint(0, s["seen"] - 1)
                                if j < s["k"]:
                                    s["sample"][j] = dt
                        else:
                            s["neg_or_zero"] += 1
                    s["prev"] = ts
                    self._stats = stats
        return self._stats


    def print_summary(self):
        stats = self.get_stats()
        header = f"{'topic':30s} {'count':>9s} {'t_min':>14s} {'t_max':>14s} {'Hz_span':>8s} {'Hz_med':>8s} {'dt[min,max]':>23s} {'bad_dt':>8s}"
        print(header)
        print("-" * len(header))
        for t in sorted(stats):
            s = stats[t]
            span = s["max_ts"] - s["min_ts"]
            hz_span = (s["good"] / span) if (s["good"] > 0 and span > 0) else 0.0
            samp = sorted(s["sample"])
            hz_med = (1.0 / samp[len(samp) // 2]) if (samp and samp[len(samp) // 2] > 0) else 0.0
            mindt = 0.0 if s["mindt"] == float("inf") else s["mindt"]
            print(f"{t:30s} {s['count']:9d} {s['min_ts']:.6f} {s['max_ts']:.6f} {hz_span:8.2f} {hz_med:8.2f} "
                  f"[{mindt:.6f},{s['maxdt']:.6f}] {s['neg_or_zero']:8d}")


if __name__ == "__main__":
    path = Path("/home/donkarlo/Dropbox/projs/research/data/self-aware-drones/ctumrs/two-drones/normal-scenario/uav1-gps-lidar-uav2-gps-lidar.yaml")
    topics = [
        "/uav1/odometry/odom_gps",
        "/uav1/rplidar/scan",
    ]
    frequency_stats = MessageFrequencyCounter(path, topics, 2000)
    frequency_stats.print_summary()
