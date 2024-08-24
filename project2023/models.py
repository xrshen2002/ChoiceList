from __future__ import division

import random
from otree.api import *
# from django.db import models
# from model_utils import FieldTracker

from otree.forms import widgets
from otree.constants import BaseConstants

from otree.models import BaseSubsession, BaseGroup, BasePlayer


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
    period_1_1 = models.IntegerField()
    period_1_2 = models.IntegerField()
    period_2_1 = models.IntegerField()
    period_2_2 = models.IntegerField()
    period_3_1 = models.IntegerField()
    period_3_2 = models.IntegerField()
    period_4_1 = models.IntegerField()
    period_4_2 = models.IntegerField()
    period_5_1 = models.IntegerField()
    period_5_2 = models.IntegerField()

    duration_1 = models.IntegerField()
    duration_2 = models.IntegerField()
    duration_3 = models.IntegerField()
    duration_4 = models.IntegerField()

    longer_period1 = models.StringField(
        choices=[
            '09-27-2025 to 10-10-2025',
            '10-05-2025 to 10-18-2025'
        ],
        widget=widgets.RadioSelect
    )

    longer_period2 = models.StringField(
        choices=[
            '02-16-2024 to 03-04-2024',
            '02-08-2024 to 02-25-2024'
        ],
        widget=widgets.RadioSelect
    )

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

    cert12 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert13 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert14 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert15 = models.IntegerField(
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

    cert22 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert23 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert24 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert25 = models.IntegerField(
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

    cert32 = models.IntegerField(
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

    cert42 = models.IntegerField(
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

    cert52 = models.IntegerField(
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

    cert62 = models.IntegerField(
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

    cert72 = models.IntegerField(
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

    cert82 = models.IntegerField(
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

    cert92 = models.IntegerField(
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

    cert102 = models.IntegerField(
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

    cert112 = models.IntegerField(
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

    cert122 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert130 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert131 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert132 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert140 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert141 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert142 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert150 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert151 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert152 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert160 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert161 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert162 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert170 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert171 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert172 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert180 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert181 = models.IntegerField(
        label="",
        choices=[(i, f"{i}%") for i in range(0, 101, 10)],
        widget=widgets.RadioSelectHorizontal
    )

    cert182 = models.IntegerField(
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

    c49 = models.IntegerField(initial=-1)

    c50 = models.IntegerField(initial=-1)

    c51 = models.IntegerField(initial=-1)

    c52 = models.IntegerField(initial=-1)

    c53 = models.IntegerField(initial=-1)

    c54 = models.IntegerField(initial=-1)

    c55 = models.IntegerField(initial=-1)

    c56 = models.IntegerField(initial=-1)

    c57 = models.IntegerField(initial=-1)

    c58 = models.IntegerField(initial=-1)

    c59 = models.IntegerField(initial=-1)

    c60 = models.IntegerField(initial=-1)

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
