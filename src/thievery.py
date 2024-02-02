from dataclasses import dataclass


@dataclass
class Crime:
    min_casing: int
    max_casing: int
    casing_drop: int
    master_thief_gain: int
    echo_gain: float
    punishing: bool = False

    def expected_casing_cost(self, max_failures_considered: int = 1_000_000) -> float:
        if not self.punishing:
            success_prob = 1.0 - 0.1 * (self.max_casing - self.min_casing)
            expected_casing_cost = sum(range(self.min_casing + 1)) * success_prob
            for attempt in range(2, max_failures_considered):
                attempt_prob = (1 - success_prob) ** (attempt - 1) * success_prob
                attempt_cost = sum(range(self.min_casing + 1)) + self.casing_drop * (
                    attempt - 1
                )
                expected_casing_cost += attempt_prob * attempt_cost
            return expected_casing_cost
        else:
            return sum(range(self.max_casing + 1))

    def expected_master_thief_gain_per_casing(self) -> float:
        return self.master_thief_gain / self.expected_casing_cost()

    def expected_echo_gain(self) -> float:
        return self.echo_gain / self.expected_casing_cost()


crimes = {
    "carnival easy": Crime(
        min_casing=5,
        max_casing=8,
        casing_drop=5,
        master_thief_gain=1,
        echo_gain=100 * 0.01 + 100 * 0.01 + 100 * 0.01 + 100 * 0.01 + 16 * 0.02,
    ),
    "carnival hard": Crime(
        min_casing=5,
        max_casing=12,
        casing_drop=10,
        master_thief_gain=2,
        echo_gain=200 * 0.01 + 200 * 0.01 + 200 * 0.01 + 200 * 0.01 + 18 * 0.02,
    ),
    "decency easy": Crime(
        min_casing=7,
        max_casing=10,
        casing_drop=7,
        master_thief_gain=2,
        echo_gain=59 * 0.04 + 200 * 0.02 + 40 * 0.05,
    ),
    "decency hard": Crime(
        min_casing=7,
        max_casing=14,
        casing_drop=10,
        master_thief_gain=3,
        echo_gain=100 * 0.04 + 5 * 0.2 + 80 * 0.05 + 200 * 0.02,
    ),
    "revolution easy": Crime(
        min_casing=9,
        max_casing=12,
        casing_drop=9,
        master_thief_gain=3,
        echo_gain=200 * 0.04 + 90 * 0.05,
    ),
    "revolution hard": Crime(
        min_casing=11,
        max_casing=16,
        casing_drop=10,
        master_thief_gain=4,
        echo_gain=300 * 0.04 + 200 * 0.02,
    ),
    "glim easy": Crime(
        min_casing=9,
        max_casing=12,
        casing_drop=9,
        master_thief_gain=3,
        echo_gain=1296 * 0.01,
    ),
    "glim hard": Crime(
        min_casing=11,
        max_casing=16,
        casing_drop=10,
        master_thief_gain=4,
        echo_gain=1872 * 0.01,
    ),
    "duchess easy": Crime(
        min_casing=11,
        max_casing=14,
        casing_drop=11,
        master_thief_gain=4,
        echo_gain=300 * 0.05 + 50 * 0.02 + 242 * 0.01 + 2 * 0.15,
    ),
    "duchess hard": Crime(
        min_casing=11,
        max_casing=16,
        casing_drop=10,
        master_thief_gain=5,
        echo_gain=1000 * 0.01 + 1000 * 0.01 + 5 * 0.01,
    ),
    "brass embassey": Crime(
        min_casing=13,
        max_casing=18,
        casing_drop=20,
        master_thief_gain=7,
        echo_gain=1000 * 0.01 + 500 * 0.02 + 40 * 0.2 + 10 * 0.12 + 25 * 0.04,
        punishing=True,
    ),
    "bazaar": Crime(
        min_casing=15,
        max_casing=20,
        casing_drop=20,
        master_thief_gain=9,
        echo_gain=16 * 2.50,
        punishing=True,
    ),
}

for name, crime in crimes.items():
    print(
        f"{name} master thief eff={crime.expected_master_thief_gain_per_casing():.4f} echo eff={crime.expected_echo_gain():.3f}"
    )
