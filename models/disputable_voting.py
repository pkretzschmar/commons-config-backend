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
        self.output_dict['Input'] = {
            'SupportRequired': self.support_required,
            'MinimumQuorum': self.minimum_quorum,
            'VoteDuration': self.vote_duration,
            'DelegatedVotingPeriod': self.delegated_voting_period,
            'QuietEndingPeriod': self.quiet_ending_period,
            'QuietEndingExtension': self.quiet_ending_extension,
            'ExecutionDelay': self.execution_delay
        }

    def get_data(self):
        # Bar Chart Data
        bar_chart_items = {
            'TotalProposalProcess': {
                'NonQuietVotingPeriod': self.non_quiet_voting_period,
                'QuietEndingPeriod': self.quiet_ending_period,
                'ExecutionDelay': self.execution_delay
            },
            'DelegatedVoting': {
                'DelegatedVotingPeriod': self.delegated_voting_period
            },
            'ProposalProcessWithExtension': {
                'VoteDuration': self.vote_duration,
                'QuietEndingExtension': self.quiet_ending_extension,
                'ExecutionDelay': self.execution_delay
            },
            'VoteDuration': self.vote_duration,
        }
        self.output_dict['Output'] = {'BarChart': bar_chart_items}

        # Pie Chart Data
        pie_chart_items = {
            'NonQuietVotingPeriod': self.non_quiet_voting_period,
            'QuietEndingPeriod': self.quiet_ending_period,
            'QuietEndingExtension': self.quiet_ending_extension,
            'ExecutionDelay': self.execution_delay
        }
        self.output_dict['Output']['PieChart'] = pie_chart_items

        return self.output_dict
