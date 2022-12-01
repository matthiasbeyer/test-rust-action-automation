# -*- coding: utf-8 -*-

# This is a backport of the similar named python module of gitlint from main:
#
#   https://github.com/jorisroovers/gitlint/blob/main/gitlint-core/gitlint/contrib/rules/disallow_cleanup_commits.py
#
# This file is licensed as MIT as of the https://github.com/jorisroovers/gitlint
# project.
#
# TODO: Remove this file if gitlint gets released as 0.18.0
#

from gitlint.rules import CommitRule, RuleViolation


class DisallowCleanupCommits(CommitRule):
    """This rule checks the commits for "fixup!"/"squash!"/"amend!" commits
    and rejects them.
    """

    name = "contrib-disallow-cleanup-commits"

    id = "UC2"

    def validate(self, commit):
        if commit.is_fixup_commit:
            return [RuleViolation(self.id, "Fixup commits are not allowed", line_nr=1)]

        if commit.is_squash_commit:
            return [RuleViolation(self.id, "Squash commits are not allowed", line_nr=1)]

        if commit.message.title.startswith("amend!"):
            return [RuleViolation(self.id, "Amend commits are not allowed", line_nr=1)]
