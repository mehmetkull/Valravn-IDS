"""Small, non-production example of one sliding-window summary."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PacketEvent:
    timestamp: float
    size: int
    destination_port: int


def summarize(events: list[PacketEvent], now: float, seconds: float) -> dict[str, float]:
    active = [event for event in events if now - seconds < event.timestamp <= now]
    return {
        "packet_rate": len(active) / seconds,
        "byte_rate": sum(event.size for event in active) / seconds,
        "unique_destination_ports": float(len({event.destination_port for event in active})),
    }


if __name__ == "__main__":
    demo = [PacketEvent(9.2, 60, 80), PacketEvent(9.7, 60, 443), PacketEvent(10.0, 120, 80)]
    print(summarize(demo, now=10.0, seconds=1.0))
