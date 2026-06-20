import os


def save_markdown(report, filename="research_report.md"):

    os.makedirs("outputs", exist_ok=True)

    path = os.path.join("outputs", filename)

    with open(path, "w", encoding="utf-8") as file:
        file.write(report)

    return path