import pandas as pd


class DisputableVotingModel:
    def __init__(self,
                 support_required=None,
                 minimum_quorum=None,
                 vote_duration=None,
                 delegated_voting_period=None,
                 quiet_ending_period=None,
                 quiet_ending_extension=None,
                 execution_delay=None):
        self.support_required = support_required if support_required is not None else 0.4
        self.minimum_quorum = minimum_quorum if minimum_quorum is not None else 0.1
        self.vote_duration = vote_duration if vote_duration is not None else 6
        self.delegated_voting_period = delegated_voting_period if delegated_voting_period is not None else 3
        self.quiet_ending_period = quiet_ending_period if quiet_ending_period is not None else 2
        self.quiet_ending_extension = quiet_ending_extension if quiet_ending_extension is not None else 1
        self.execution_delay = execution_delay if execution_delay is not None else 1
        self.non_quiet_voting_period = max(self.vote_duration - self.quiet_ending_period, 0)
        self.output_dict = {}
        self.output_dict['input'] = {
            'support-required': self.support_required,
            'minimum-quorum': self.minimum_quorum,
            'vote-duration': self.vote_duration,
            'delegated-voting-period': self.delegated_voting_period,
            'quiet-ending-period': self.quiet_ending_period,
            'quiet-ending-extension': self.quiet_ending_extension,
            'execution-delay': self.execution_delay
        }

    def get_data(self):
        # Bar Chart Data
        bar_chart_items = {
            'total-proposal-process': {
                'non-quiet-voting-period': self.non_quiet_voting_period,
                'quiet-ending-period': self.quiet_ending_period,
                'execution-delay': self.execution_delay
            },
            'delegated-voting': {
                'delegated-voting-period': self.delegated_voting_period
            },
            'proposal-process-with-extension': {
                'voteduration': self.vote_duration,
                'quiet-ending_extension': self.quiet_ending_extension,
                'execution-delay': self.execution_delay
            },
            'vote-duration': self.vote_duration,
        }
        self.output_dict['output'] = {'bar-chart': bar_chart_items}

        # Pie Chart Data
        pie_chart_items = {
            'non-quiet-voting-period': self.non_quiet_voting_period,
            'quiet-ending-period': self.quiet_ending_period,
            'quiet-ending-extension': self.quiet_ending_extension,
            'execution-delay': self.execution_delay
        }
        self.output_dict['output']['pie-chart'] = pie_chart_items

        return self.output_dict
