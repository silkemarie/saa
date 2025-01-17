from dataclasses import dataclass
from saa.core.language import Luga


@dataclass
class Danish(Luga):
    time = {
        "to": "{minute} is_minutes i {hour}",
        "past": "{minute} is_minutes over {hour}",
        0: "klokken {hour}",
        15: "kvart over {hour}",
        45: "kvart i {hour}",
        30: "halv{hour}",
    }

    number_connector = "og"
    connect_format = "{2}{1}{0}"
    numbers = {
        0: "nul",
        1: "en",
        2: "to",
        3: "tre",
        4: "fire",
        5: "fem",
        6: "seks",
        7: "syv",
        8: "otte",
        9: "ni",
        10: "ti",
        11: "elleve",
        12: "tolv",
        13: "tretten",
        14: "fjorten",
        15: "femten",
        16: "seksten",
        17: "sytten",
        18: "atten",
        19: "nitten",
        20: "tyve",
        30: "tredive",
        40: "fyrre",
        50: "halvtreds",
    }

    @staticmethod
    def time_logic(hour, minute) -> tuple[int, int, str, str]:
        is_to = "to" if minute >= 30 else "past"
        is_minutes = "minutter" if minute > 1 else "minut"

        if hour > 12:
            hour = hour - 12

        if is_to == "to":
            hour += 1
            minute = 60 - minute

        return hour, minute, is_to, is_minutes

    @staticmethod
    def post_logic(text):
        text = " ".join(
            "et" if word == "en" else word.replace("en", "et")
            for word in text.split()
            if "enog" not in word
        )
        return text


class Language(Danish):
    pass
