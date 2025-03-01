from math import floor

from typing import List
import random
from random import choice

from ._builtin import Page, WaitPage
from .choices import ChoiceManager

from .config import GAIN_PER_WEEK, NUM_WEEKS, NUM_DAYS

from . import models
from .models import Constants


class AttentionCheck2(Page):
    form_model = 'player'
    form_fields = ['question_4_answer']

    def vars_for_template(self):
        return {
            'question_4_text': Constants.QUESTION_4_TEXT,
            'choices_4': [f"{i}" for i in range(30, 40, 1)]  # 这是第二个问题的选项
        }

    def before_next_page(self):
        # 检查玩家的回答是否正确
        if self.player.question_4_answer == Constants.QUESTION_4_ANSWER:
            self.player.participant.vars['failed_attention_check2'] = False
        else:
            self.player.participant.vars['failed_attention_check2'] = True

    def app_after_this_page(self, upcoming_apps):
        if self.player.participant.vars.get('failed_attention_check2', False):
            return upcoming_apps[-1]  # 跳转到实验的最后一个应用

class AttentionCheck3(Page):
    form_model = 'player'
    form_fields = ['question_5_answer']

    def vars_for_template(self):
        return {
            'question_5_text': Constants.QUESTION_5_TEXT,
            'choices_5': [f"{i}" for i in range(10, 25, 2)]
        }

    def before_next_page(self):
        # 检查玩家的回答是否正确
        if self.player.question_5_answer == Constants.QUESTION_5_ANSWER:
            self.player.participant.vars['failed_attention_check3'] = False
        else:
            self.player.participant.vars['failed_attention_check3'] = True

    def app_after_this_page(self, upcoming_apps):
        if self.player.participant.vars.get('failed_attention_check3', False):
            return upcoming_apps[-1]  # 跳转到实验的最后一个应用

class AttentionCheck4(Page):
    form_model = 'player'
    form_fields = ['question_6_answer']

    def vars_for_template(self):
        return {
            'question_6_text': Constants.QUESTION_6_TEXT,
            'choices_6': [f"{i}" for i in range(65, 95, 3)]
        }

    def before_next_page(self):
        # 检查玩家的回答是否正确
        if self.player.question_6_answer == Constants.QUESTION_6_ANSWER:
            self.player.participant.vars['failed_attention_check4'] = False
        else:
            self.player.participant.vars['failed_attention_check4'] = True

    def app_after_this_page(self, upcoming_apps):
        if self.player.participant.vars.get('failed_attention_check4', False):
            return upcoming_apps[-1]  # 跳转到实验的最后一个应用

class Checkin(Page):
    pass


class Instruction1(Page):
    pass

class Instruction2(Page):
    pass

class Instruction3(Page):
    pass

class Instruction4(Page):
    pass

class Demographic(Page):
    form_model = "player"
    form_fields = ["age", "gender", "education", "employment", "income", "zipcode"]


class SliderPage1(Page):
    form_model = 'player'
    form_fields = ['period_1_1', 'period_1_2']
    # form_fields = ['period_1_1', 'period_1_2', 'period_2_1', 'period_2_2', 'period_3_1', 'period_3_2', 'period_4_1',
    #                'period_4_2', 'period_5_1', 'period_5_2']

    def before_next_page(self):
        # Add any logic needed before moving to the next page
        pass

class SliderPage2(Page):
    form_model = 'player'
    form_fields = ['period_2_1', 'period_2_2']

    def before_next_page(self):
        # Add any logic needed before moving to the next page
        pass

class SliderPage3(Page):
    form_model = 'player'
    form_fields = ['period_3_1', 'period_3_2']

    def before_next_page(self):
        # Add any logic needed before moving to the next page
        pass

class CalcuDurationPage1(Page):
    form_model = 'player'
    form_fields = ['duration_1', 'duration_2']

    def before_next_page(self):
        # Custom code can be added here if needed
        pass

class CalcuDurationPage2(Page):
    form_model = 'player'
    form_fields = ['duration_3', 'duration_4']

    def before_next_page(self):
        # Custom code can be added here if needed
        pass

class CalcuDurationPage3(Page):
    form_model = 'player'
    form_fields = ['duration_5', 'duration_6']

    def before_next_page(self):
        # Custom code can be added here if needed
        pass

class ChooseDurationPage1(Page):
    form_model = 'player'
    form_fields = ['longer_period1']

    def before_next_page(self):
        # Custom code can be added here if needed
        pass

class ChooseDurationPage2(Page):
    form_model = 'player'
    form_fields = ['longer_period2']

    def before_next_page(self):
        # Custom code can be added here if needed
        pass

class ChooseDurationPage3(Page):
    form_model = 'player'
    form_fields = ['longer_period3']

    def before_next_page(self):
        # Custom code can be added here if needed
        pass
class Think2(Page):
    form_model = 'player'
    form_fields = ['time_thinking_choice_2', 'time_thinking_other_2']
    # def vars_for_template(self):
    #     """
    #     在模板 think.html 中，如果需要回显 CL11 中记录的文本
    #     （chosen_text_either, chosen_text_other），在这里传给模板
    #     """
    #     return {
    #         'previous_either': self.player.chosen_text_either,
    #         'previous_other': self.player.chosen_text_other
    #     }
    def before_next_page(self):
        """
        - 如果用户没有选择 'other'，就把 time_thinking_other 字段置空，
          避免存入无效文本。
        - 如果用户选择了 'other'，但没有填写任何有效内容 (只输入空格等)，
          则需要返回错误信息，提示补充填写。
        """
        if self.player.time_thinking_choice_2 != 'other':
            # 如果用户没有选择 "other"，清空输入框结果
            self.player.time_thinking_other_2 = ''
        elif not self.player.time_thinking_other_2.strip():
            # 如果选择了 "other"，但输入框为空或仅包含空格，抛出错误
            return "Please specify your thinking process if you chose 'Other'."

class Think(Page):
    form_model = 'player'
    form_fields = ['time_thinking_choice', 'time_thinking_other']

    def vars_for_template(self):
        return {
            'selected_row': self.player.c13,
            'random_sequence': random.choice([1, 2]),
        }

class Think2(Page):
    form_model = 'player'
    form_fields = ['time_thinking_choice_2', 'time_thinking_other_2']

    def vars_for_template(self):
        return {
            'selected_row': self.player.c53,
            'random_sequence': random.choice([1, 2]),
        }

class CL10(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class TestPage(Page):
    form_model = 'player'
    form_fields = ['chosen_text_either']  # 只提交这一个字段

    def vars_for_template(self):
        return {}

    def before_next_page(self):
        print("===== DEBUG: before_next_page =====")
        print("chosen_text_either from form:", self.player.chosen_text_either)


class CL11(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL12(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL13(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL14(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL15(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL16(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL17(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL20(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL21(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL22(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL23(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL24(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL25(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL26(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL27(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL28(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL29(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL210(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL30(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL31(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL32(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL40(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL41(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL42(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL50(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL51(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL52(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL60(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL61(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL62(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL70(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL10d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL11d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL12d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL13d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL14d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL15d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL16d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL17d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL20d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL21d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL22d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL23d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL24d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL25d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL26d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL27d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL28d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL29d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL210d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL30d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL31d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL32d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL40d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL41d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL42d(Page):

    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL50d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL51d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL52d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL60d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()


class CL61d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL62d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL70d(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
        return [dynamic_field]

    def vars_for_template(self):
        manager = ChoiceManager(self.player)
        day_range = manager.get_day_range()
        day_start = day_range[0]
        day_end = day_range[-1]
        option_a_date = day_range[:]
        option_b_date = day_range[:]
        day_gain = zip(option_a_date, option_b_date)

        return {
            'progress': self.player.get_current_step() / 6 * 100,
            'var_name': manager.get_step().get_field(),
            'day_start': day_start,
            'day_end': day_end,
            'day_gain': day_gain,
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        if index == -1:
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

class Results(Page):
    pass

# choicelist_groups = [
#     [AttentionCheck2, ChoiceList7, ChoiceList9],
#     [AttentionCheck3, ChoiceList10, ChoiceList12],
# ]

# chosen_group = choice(choicelist_groups)

page_sequence = [
    CL42d,
    CL24d,
    CL26d,
    CL50d,
    CL14d,
    CL21d,
    CL51d,
    CL13d,
    CL10d,
    CL25d,
    CL17d,
    CL52d,
    CL16d,
    CL61d,
    CL30d,
    CL29d,
    CL12d,
    CL23d,
    CL11d,
    CL62d,
    CL22d,
    CL31d,
    CL40d,
    CL20d,
    CL27d,
    CL15d,
    CL28d,
    CL32d,
    CL210d,
    CL41d,
    CL60d,
    Instruction1,
    AttentionCheck2,
    CL51,
    CL11,
    CL32,
    CL14,
    CL26,
    CL28,
    CL42,
    CL60,
    CL27,
    CL12,
    CL41,
    CL50,
    CL25,
    CL52,
    CL20,
    CL30,
    CL10,
    CL22,
    CL17,
    CL61,
    CL210,
    CL16,
    CL31,
    CL24,
    CL13,
    CL23,
    CL40,
    CL62,
    CL29,
    CL15,
    CL21,
    Think,
    Think2,
    CalcuDurationPage1,
    ChooseDurationPage1,
    SliderPage1,
    CalcuDurationPage2,
    ChooseDurationPage2,
    SliderPage2,
    CalcuDurationPage3,
    ChooseDurationPage3,
    SliderPage3,

    # TestPage,

    # Instruction3,

    # Instruction4,


    # Instruction1,
    # AttentionCheck2,

    # Instruction3,

    # Instruction4,
    # Instruction2,
    # AttentionCheck3,


    # *chosen_group,

    # AttentionCheck4,

    Demographic,
    Results,
    ResultsWaitPage,
]

