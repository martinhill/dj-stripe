# -*- coding: utf-8 -*-
"""
.. module:: djstripe.forms
   :synopsis: dj-stripe Forms.

.. moduleauthor:: Daniel Greenfeld (@pydanny)

"""

from django import forms
from .models import Plan


PLAN_CHOICES = [(plan.stripe_id, plan.name) for plan in Plan.objects.all()]


class PlanForm(forms.Form):
    plan = forms.ChoiceField(choices=PLAN_CHOICES)


class CancelSubscriptionForm(forms.Form):
    pass
