from math import floor

from typing import List
import random
from random import choice

from ._builtin import Page, WaitPage
from .choices import ChoiceManager
from .models import Constants

from .config import GAIN_PER_WEEK, NUM_WEEKS, NUM_DAYS


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

class Demographic(Page):
    form_model = "player"
    form_fields = ["age", "gender", "education", "employment", "income", "zipcode"]

class CL10(Page):

    form_model = 'player'
    form_fields = ['cert10']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
    #     manager = ChoiceManager(self.player)
    #     return [manager.get_step().get_field()]
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert10':
            return [dynamic_field, 'cert10']
        else:
            return ['cert10']

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
            # 'question_7_text': Constants.QUESTION_7_TEXT
            # 'choices_7': [f"{i}%" for i in range(0, 101, 10)]  # 这是第二个问题的选项
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL11(Page):

    form_model = 'player'
    form_fields = ['cert11']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert11':
            return [dynamic_field, 'cert11']
        else:
            return ['cert11']

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
    form_fields = ['cert20']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert20':
            return [dynamic_field, 'cert20']
        else:
            return ['cert20']

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
    form_fields = ['cert21']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert21':
            return [dynamic_field, 'cert21']
        else:
            return ['cert21']

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
    form_fields = ['cert30']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert30':
            return [dynamic_field, 'cert30']
        else:
            return ['cert30']

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
    form_fields = ['cert31']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert31':
            return [dynamic_field, 'cert31']
        else:
            return ['cert31']

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
    form_fields = ['cert40']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert40':
            return [dynamic_field, 'cert40']
        else:
            return ['cert40']

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
    form_fields = ['cert41']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert41':
            return [dynamic_field, 'cert41']
        else:
            return ['cert41']

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
    form_fields = ['cert50']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert50':
            return [dynamic_field, 'cert50']
        else:
            return ['cert50']

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
    form_fields = ['cert51']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert51':
            return [dynamic_field, 'cert51']
        else:
            return ['cert51']

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
    form_fields = ['cert60']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert60':
            return [dynamic_field, 'cert60']
        else:
            return ['cert60']

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
    form_fields = ['cert61']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert61':
            return [dynamic_field, 'cert61']
        else:
            return ['cert61']

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
    form_fields = ['cert70']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert70':
            return [dynamic_field, 'cert70']
        else:
            return ['cert70']

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

class CL71(Page):

    form_model = 'player'
    form_fields = ['cert71']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert71':
            return [dynamic_field, 'cert71']
        else:
            return ['cert71']

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

class CL80(Page):

    form_model = 'player'
    form_fields = ['cert80']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert80':
            return [dynamic_field, 'cert80']
        else:
            return ['cert80']

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

class CL81(Page):

    form_model = 'player'
    form_fields = ['cert81']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert81':
            return [dynamic_field, 'cert81']
        else:
            return ['cert81']

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

class CL90(Page):

    form_model = 'player'
    form_fields = ['cert90']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert90':
            return [dynamic_field, 'cert90']
        else:
            return ['cert90']

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

class CL91(Page):

    form_model = 'player'
    form_fields = ['cert91']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert91':
            return [dynamic_field, 'cert91']
        else:
            return ['cert91']

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

class CL100(Page):

    form_model = 'player'
    form_fields = ['cert100']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert100':
            return [dynamic_field, 'cert100']
        else:
            return ['cert100']

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
class CL101(Page):

    form_model = 'player'
    form_fields = ['cert101']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert101':
            return [dynamic_field, 'cert101']
        else:
            return ['cert101']

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
class CL110(Page):

    form_model = 'player'
    form_fields = ['cert110']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert110':
            return [dynamic_field, 'cert110']
        else:
            return ['cert110']

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
class CL111(Page):

    form_model = 'player'
    form_fields = ['cert111']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert111':
            return [dynamic_field, 'cert111']
        else:
            return ['cert111']

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
class CL120(Page):

    form_model = 'player'
    form_fields = ['cert120']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert120':
            return [dynamic_field, 'cert120']
        else:
            return ['cert120']

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
class CL121(Page):

    form_model = 'player'
    form_fields = ['cert121']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert121':
            return [dynamic_field, 'cert121']
        else:
            return ['cert121']

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
class CL10l(Page):

    form_model = 'player'
    form_fields = ['cert10l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
    #     manager = ChoiceManager(self.player)
    #     return [manager.get_step().get_field()]
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert10l':
            return [dynamic_field, 'cert10l']
        else:
            return ['cert10l']

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
            # 'question_7_text': Constants.QUESTION_7_TEXT
            # 'choices_7': [f"{i}%" for i in range(0, 101, 10)]  # 这是第二个问题的选项
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL11l(Page):

    form_model = 'player'
    form_fields = ['cert11l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert11l':
            return [dynamic_field, 'cert11l']
        else:
            return ['cert11l']

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

class CL20l(Page):

    form_model = 'player'
    form_fields = ['cert20l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert20l':
            return [dynamic_field, 'cert20l']
        else:
            return ['cert20l']

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

class CL21l(Page):

    form_model = 'player'
    form_fields = ['cert21l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert21l':
            return [dynamic_field, 'cert21l']
        else:
            return ['cert21l']

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

class CL30l(Page):

    form_model = 'player'
    form_fields = ['cert30l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert30l':
            return [dynamic_field, 'cert30l']
        else:
            return ['cert30l']

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

class CL31l(Page):

    form_model = 'player'
    form_fields = ['cert31l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert31l':
            return [dynamic_field, 'cert31l']
        else:
            return ['cert31l']

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

class CL40l(Page):

    form_model = 'player'
    form_fields = ['cert40l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert40l':
            return [dynamic_field, 'cert40l']
        else:
            return ['cert40l']

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

class CL41l(Page):

    form_model = 'player'
    form_fields = ['cert41l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert41l':
            return [dynamic_field, 'cert41l']
        else:
            return ['cert41l']

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

class CL50l(Page):

    form_model = 'player'
    form_fields = ['cert50l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert50l':
            return [dynamic_field, 'cert50l']
        else:
            return ['cert50l']

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

class CL51l(Page):

    form_model = 'player'
    form_fields = ['cert51l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert51l':
            return [dynamic_field, 'cert51l']
        else:
            return ['cert51l']

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

class CL60l(Page):

    form_model = 'player'
    form_fields = ['cert60l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert60l':
            return [dynamic_field, 'cert60l']
        else:
            return ['cert60l']

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

class CL61l(Page):

    form_model = 'player'
    form_fields = ['cert61l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert61l':
            return [dynamic_field, 'cert61l']
        else:
            return ['cert61l']

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

class CL70l(Page):

    form_model = 'player'
    form_fields = ['cert70l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert70l':
            return [dynamic_field, 'cert70l']
        else:
            return ['cert70l']

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

class CL71l(Page):

    form_model = 'player'
    form_fields = ['cert71l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert71l':
            return [dynamic_field, 'cert71l']
        else:
            return ['cert71l']

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

class CL80l(Page):

    form_model = 'player'
    form_fields = ['cert80l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert80l':
            return [dynamic_field, 'cert80l']
        else:
            return ['cert80l']

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

class CL81l(Page):

    form_model = 'player'
    form_fields = ['cert81l']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert81l':
            return [dynamic_field, 'cert81l']
        else:
            return ['cert81l']

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

class CL10s(Page):

    form_model = 'player'
    form_fields = ['cert10s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
    #     manager = ChoiceManager(self.player)
    #     return [manager.get_step().get_field()]
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert10s':
            return [dynamic_field, 'cert10s']
        else:
            return ['cert10s']

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
            # 'question_7_text': Constants.QUESTION_7_TEXT
            # 'choices_7': [f"{i}%" for i in range(0, 101, 10)]  # 这是第二个问题的选项
        }

    def before_next_page(self):
        manager = ChoiceManager(self.player)

        # we fix the computed value as the client gives us just
        # the index of the selected option - which is not directly a week
        # the index is 1-based so we have subtract 1

        field_name = manager.get_step().get_field()
        index = getattr(self.player, field_name) - 1
        day_range = manager.get_day_range()

        # the number of selectable options is len(day_range) + 1
        if index == -1:
            # selection is invalid - we cannot handle this case further
            # as it would lead to invalid ranges in the future
            setattr(self.player, field_name, index)
            self.player.cancel_game()
        else:
            switch_lower_bound = day_range[index]
            setattr(self.player, field_name, switch_lower_bound)
            self.player.goto_next_step()

class CL11s(Page):

    form_model = 'player'
    form_fields = ['cert11s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert11s':
            return [dynamic_field, 'cert11s']
        else:
            return ['cert11s']

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

class CL20s(Page):

    form_model = 'player'
    form_fields = ['cert20s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert20s':
            return [dynamic_field, 'cert20s']
        else:
            return ['cert20s']

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

class CL21s(Page):

    form_model = 'player'
    form_fields = ['cert21s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert21s':
            return [dynamic_field, 'cert21s']
        else:
            return ['cert21s']

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

class CL30s(Page):

    form_model = 'player'
    form_fields = ['cert30s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert30s':
            return [dynamic_field, 'cert30s']
        else:
            return ['cert30s']

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

class CL31s(Page):

    form_model = 'player'
    form_fields = ['cert31s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert31s':
            return [dynamic_field, 'cert31s']
        else:
            return ['cert31s']

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

class CL40s(Page):

    form_model = 'player'
    form_fields = ['cert40s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert40s':
            return [dynamic_field, 'cert40s']
        else:
            return ['cert40s']

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

class CL41s(Page):

    form_model = 'player'
    form_fields = ['cert41s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert41s':
            return [dynamic_field, 'cert41s']
        else:
            return ['cert41s']

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

class CL50s(Page):

    form_model = 'player'
    form_fields = ['cert50s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert50s':
            return [dynamic_field, 'cert50s']
        else:
            return ['cert50s']

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

class CL51s(Page):

    form_model = 'player'
    form_fields = ['cert51s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert51s':
            return [dynamic_field, 'cert51s']
        else:
            return ['cert51s']

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

class CL60s(Page):

    form_model = 'player'
    form_fields = ['cert60s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert60s':
            return [dynamic_field, 'cert60s']
        else:
            return ['cert60s']

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

class CL61s(Page):

    form_model = 'player'
    form_fields = ['cert61s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert61s':
            return [dynamic_field, 'cert61s']
        else:
            return ['cert61s']

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

class CL70s(Page):

    form_model = 'player'
    form_fields = ['cert70s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert70s':
            return [dynamic_field, 'cert70s']
        else:
            return ['cert70s']

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

class CL71s(Page):

    form_model = 'player'
    form_fields = ['cert71s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert71s':
            return [dynamic_field, 'cert71s']
        else:
            return ['cert71s']

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

class CL80s(Page):

    form_model = 'player'
    form_fields = ['cert80s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert80s':
            return [dynamic_field, 'cert80s']
        else:
            return ['cert80s']

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

class CL81s(Page):

    form_model = 'player'
    form_fields = ['cert81s']

    def is_displayed(self):
        return self.player.get_current_step() != -1

    def get_form_fields(self) -> List[str]:
        manager = ChoiceManager(self.player)
        dynamic_field = manager.get_step().get_field()
    # 确保 certainty 字段总是被返回
        if dynamic_field != 'cert81s':
            return [dynamic_field, 'cert81s']
        else:
            return ['cert81s']

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
    CL10,
    CL20,
    CL30,
    CL40,
    CL11,
    CL21,
    CL31,
    CL41,
    Instruction1,
    AttentionCheck2,
    CL90,
    CL100,
    CL110,
    CL120,
    CL91,
    CL101,
    CL111,
    CL121,
    Instruction2,
    AttentionCheck3,
    CL50,
    CL60,
    CL70,
    CL80,
    CL51,
    CL61,
    CL71,
    CL81,

    # CL10l,
    # CL11l,
    # CL20l,
    # CL21l,
    # CL30l,
    # CL31l,
    # CL40l,
    # CL41l,
    # CL50l,
    # CL51l,
    # CL60l,
    # CL61l,
    # CL70l,
    # CL71l,
    # CL80l,
    # CL81l,

    # CL10s,
    # CL11s,
    # CL20s,
    # CL21s,
    # CL30s,
    # CL31s,
    # CL40s,
    # CL41s,
    # CL50s,
    # CL51s,
    # CL60s,
    # CL61s,
    # CL70s,
    # CL71s,
    # CL80s,
    # CL81s,
    # *chosen_group,

    # AttentionCheck4,
    Demographic,
    Results,
    ResultsWaitPage
]

