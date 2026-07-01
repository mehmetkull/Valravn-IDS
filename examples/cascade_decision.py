"""Educational cascade example; it does not load production models."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Thresholds:
    rf_low: float = 0.70
    rf_high: float = 0.85
    tabnet_attack: float = 0.65


def decide(rf_score: float, tabnet_score: float | None, packet_count: int) -> str:
    if packet_count < 2:
        return "insufficient_data"
    if rf_score < Thresholds.rf_low:
        return "normal_rf"
    if rf_score >= Thresholds.rf_high:
        return "attack_rf"
    if tabnet_score is None:
        raise ValueError("Gray-zone flows require a TabNet score")
    return "attack_tabnet" if tabnet_score >= Thresholds.tabnet_attack else "normal_tabnet"


if __name__ == "__main__":
    samples = [(0.08, None, 8), (0.78, 0.72, 14), (0.94, None, 30), (0.20, None, 1)]
    for sample in samples:
        print(sample, "->", decide(*sample))
