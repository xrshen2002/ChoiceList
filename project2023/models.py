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
        choices=[(f"{i}", f"{i}") for i in range(10, 25, 2)],
        label="",  # 设置问题文本
        widget=widgets.RadioSelectHorizontal  # 使用单选框
    )


    current_step = models.IntegerField(initial=1)
    """Current step the player is in
    
    Equals the elicitation round, i.e. ranges from 1 (for c12) to 5 (c78).
    """


    # IMPORTANT: DO NOT CHANGE THE VARIABLE NAMES FOR THE c values!

    c12 = models.IntegerField(initial=-1)
    """Represents the measured value of c_(1/2)"""

    c14 = models.IntegerField(initial=-1)
    """Represents the measured value of c_(1/4)"""

    c34 = models.IntegerField(initial=-1)
    """Represents the measured value of c_(3/4)"""

    c4 = models.IntegerField(initial=-1)


    c5 = models.IntegerField(initial=-1)


    c6 = models.IntegerField(initial=-1)

    c7 = models.IntegerField(initial=-1)

    c8 = models.IntegerField(initial=-1)

    c9 = models.IntegerField(initial=-1)

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
