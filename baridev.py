def solution(seconds):
    if seconds == 0:
        return "now"

    time_units = {
        "ano": 365 * 24 * 60 * 60,
        "dia": 24 * 60 * 60,
        "hora": 60 * 60,
        "minuto": 60,
        "segundo": 1,
    }

    time_components = []
    for unit, duration in time_units.items():
        if seconds >= duration:
            count = seconds // duration
            seconds %= duration
            if count > 1:
                unit += "s"
            time_components.append(f"{count} {unit}")

    return ", ".join(time_components)


seconds = int(input())
out_ = solution(seconds)
print(out_)
