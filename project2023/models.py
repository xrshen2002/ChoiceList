import random

author = 'Michael Rose <michael_rose@gmx.de>'

doc = """
otdm provides an easy way of creating experiments to measure the temporal discounting of money
using the Direct Method (DM) [Attema et al., 2016]
"""

from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer, Page
)

class Constants(BaseConstants):
    name_in_url = 'project2023'
    players_per_group = None
    num_rounds = 1

    QUESTION_4_TEXT = "Please select the number 37:"
    QUESTION_4_ANSWER = 37

    QUESTION_5_TEXT = "Please select the number 14:"
    QUESTION_5_ANSWER = 14

    QUESTION_6_TEXT = "Please select the number 71:"
    QUESTION_6_ANSWER = 71

    # QUESTION_7_TEXT = "What do the following images represent?"
    # QUESTION_7_ANSWER = "3"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.StringField(
        label="How old are you?",
        choices=["Under 18", "18-24 years old", "25-34 years old", "35-44 years old", "45-54 years old", "55-64 years old", "65+ years old"]
    )
    gender = models.StringField(
        label="How do you describe yourself?",
        choices=["Male", "Female", "Non-binary / third gender", "Prefer not to say"]
    )
    education = models.StringField(
        label="What is the highest level of education you have completed?",
        choices=["Some high school or less", "High school diploma or GED", "Some college, but no degree", "Associates or technical degree", "Bachelor’s degree", "Graduate or professional degree (MA, MS, MBA, PhD, JD, MD, DDS etc.)", "Prefer not to say"]
    )
    employment = models.StringField(
        label="What best describes your employment status over the last three months?",
        choices=["Working full-time", "Working part-time", "Unemployed and looking for work", "A homemaker or stay-at-home parent", "Student", "Retired", "Other"]
    )
    income = models.StringField(
        label="What was your total household income before taxes during the past 12 months?",
        choices=["Less than $25,000", "$25,000-$49,999", "$50,000-$74,999", "$75,000-$99,999", "$100,000-$149,999", "$150,000 or more", "Prefer not to say"]
    )
    zipcode = models.IntegerField(label="What is your US Zip Code?")


    question_4_answer = models.IntegerField(
        choices=[(f"{i}", f"{i}") for i in range(30, 41, 1)],
        label="",  # 设置问题文本
        widget=widgets.RadioSelectHorizontal  # 使用单选框
    )

    question_5_answer = models.IntegerField(
        choices=[(f"{i}", f"{i}") for i in range(10, 31, 2)],
        label="",  # 设置问题文本
        widget=widgets.RadioSelectHorizontal  # 使用单选框
    )

    question_6_answer = models.IntegerField(
        choices=[(f"{i}", f"{i}") for i in range(65, 96, 3)],
        label="",  # 设置问题文本
        widget=widgets.RadioSelectHorizontal  # 使用单选框
    )
    # question_7_answer = models.StringField(
    #     choices=[(f"{i}%", f"{i}%") for i in range(0, 101, 10)],
    #     label="",
    #     widget=widgets.RadioSelectHorizontal  # 仍然使用 widgets.RadioSelect
    # )
    cert10 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert11 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert20 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert21 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert30 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert31 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert40 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert41 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert50 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert51 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert60 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert61 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert70 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert71 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert80 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert81 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert90 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert91 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert100 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert101 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert110 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert111 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert120 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert121 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert10l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert11l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert20l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert21l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert30l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert31l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert40l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert41l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert50l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert51l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert60l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert61l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert70l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert71l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert80l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert81l = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert10s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert11s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert20s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert21s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert30s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert31s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert40s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert41s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert50s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert51s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert60s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert61s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert70s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert71s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert80s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )
    cert81s = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    current_step = models.IntegerField(initial=1)
    """Current step the player is in
    
    Equals the elicitation round, i.e. ranges from 1 (for c12) to 5 (c78).
    """


    # IMPORTANT: DO NOT CHANGE THE VARIABLE NAMES FOR THE c values!

    c1 = models.IntegerField(initial=-1)

    c2 = models.IntegerField(initial=-1)

    c3 = models.IntegerField(initial=-1)

    c4 = models.IntegerField(initial=-1)

    c5 = models.IntegerField(initial=-1)

    c6 = models.IntegerField(initial=-1)

    c7 = models.IntegerField(initial=-1)

    c8 = models.IntegerField(initial=-1)

    c9 = models.IntegerField(initial=-1)

    c10 = models.IntegerField(initial=-1)

    c11 = models.IntegerField(initial=-1)

    c12 = models.IntegerField(initial=-1)

    c13 = models.IntegerField(initial=-1)

    c14 = models.IntegerField(initial=-1)

    c15 = models.IntegerField(initial=-1)

    c16 = models.IntegerField(initial=-1)

    c17 = models.IntegerField(initial=-1)

    c18 = models.IntegerField(initial=-1)

    c19 = models.IntegerField(initial=-1)

    c20 = models.IntegerField(initial=-1)

    c21 = models.IntegerField(initial=-1)

    c22 = models.IntegerField(initial=-1)

    c23 = models.IntegerField(initial=-1)

    c24 = models.IntegerField(initial=-1)

    c25 = models.IntegerField(initial=-1)

    c26 = models.IntegerField(initial=-1)

    c27 = models.IntegerField(initial=-1)

    c28 = models.IntegerField(initial=-1)

    c29 = models.IntegerField(initial=-1)

    c30 = models.IntegerField(initial=-1)

    c31 = models.IntegerField(initial=-1)

    c32 = models.IntegerField(initial=-1)

    c33 = models.IntegerField(initial=-1)

    c34 = models.IntegerField(initial=-1)

    c35 = models.IntegerField(initial=-1)

    c36 = models.IntegerField(initial=-1)

    c37 = models.IntegerField(initial=-1)

    c38 = models.IntegerField(initial=-1)

    c39 = models.IntegerField(initial=-1)

    c40 = models.IntegerField(initial=-1)

    c41 = models.IntegerField(initial=-1)

    c42 = models.IntegerField(initial=-1)

    c43 = models.IntegerField(initial=-1)

    c44 = models.IntegerField(initial=-1)

    c45 = models.IntegerField(initial=-1)

    c46 = models.IntegerField(initial=-1)

    c47 = models.IntegerField(initial=-1)

    c48 = models.IntegerField(initial=-1)

    def goto_next_step(self) -> None:
        """Advances the player to the next step

        Should be called after each `ChoiceListPage`
        """
        self.current_step = self.current_step + 1

    def cancel_game(self) -> None:
        """Sets the indicator that an invalid choice occurred"""
        self.current_step = -1

    def get_current_step(self) -> int:
        """Get the current step the player is in
        :return: current step (1-based)
        """
        return self.current_step
