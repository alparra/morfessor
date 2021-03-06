#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Morfessor 2.0 - Python implementation of the Morfessor method
"""
import logging


__all__ = ['MorfessorException', 'ArgumentException', 'MorfessorIO',
           'BaselineModel', 'main', 'get_default_argparser', 'main_evaluation',
           'get_evaluation_argparser']

__version__ = '2.0.6'
__author__ = 'Sami Virpioja, Peter Smit, Stig-Arne Grönroos'
__author_email__ = "morpho@aalto.fi"

_logger = logging.getLogger(__name__)


def get_version():
    return __version__

# The public api imports need to be at the end of the file,
# so that the package global names are available to the modules
# when they are imported.

from .baseline import BaselineModel, FixedCorpusWeight, AnnotationCorpusWeight, \
    NumMorphCorpusWeight, MorphLengthCorpusWeight
from .cmd import main, get_default_argparser, main_evaluation, \
    get_evaluation_argparser
from .exception import MorfessorException, ArgumentException
from .io import MorfessorIO
from .utils import _progress
from .evaluation import MorfessorEvaluation, MorfessorEvaluationResult
