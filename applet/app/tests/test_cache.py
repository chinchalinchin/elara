import json
import pytest
import sys
import os

from unittest.mock import patch, mock_open

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))

sys.path.insert(0, project_root)

from objects.cache import Cache
from properties import CacheProps

# Sample Cache Data for testing (no longer needs to be in a file)
TEST_CACHE_DATA = {
    CacheProps.MODELS.value: {
        CacheProps.MODELS_BASE.value: [
            {
                "path": "models/gemini-2.0-flash-exp",
                "version": "2.0",
                "input_token_limit": 1048576,
                "output_token_limit": 8192
            },
            {
                "path": "models/gemini-exp-1206",
                "version": "exp_1206",
                "input_token_limit": 2097152,
                "output_token_limit": 8192
            },
            {
                "path": "models/gemini-exp-1121",
                "version": "exp-1206",
                "input_token_limit": 2097152,
                "output_token_limit": 8192
            },
            {
                "path": "models/gemini-exp-1114",
                "version": "exp-1206",
                "input_token_limit": 2097152,
                "output_token_limit": 8192
            },
            {
                "path": "models/gemini-2.0-flash-thinking-exp-01-21",
                "version": "2.0-exp-01-21",
                "input_token_limit": 1048576,
                "output_token_limit": 65536
            },
            {
                "path": "models/gemini-2.0-flash-thinking-exp",
                "version": "2.0-exp-01-21",
                "input_token_limit": 1048576,
                "output_token_limit": 65536
            },
            {
                "path": "models/gemini-2.0-flash-thinking-exp-1219",
                "version": "2.0",
                "input_token_limit": 1048576,
                "output_token_limit": 65536
            }
        ],
        CacheProps.MODELS_TUNING.value: [
            {
                "path": "models/gemini-1.5-flash-001-tuning",
                "version": "001",
                "input_token_limit": 16384,
                "output_token_limit": 8192
            }
        ],
        CacheProps.MODELS_TUNED.value: [
            {
                "path": "tunedModels/elara-a38gqsr3zzw8"
            },
            {
                "path": "tunedModels/axiom-rx8g5v830mqn"
            }
        ]
    },
    CacheProps.TUNING_MODEL.value: "models/gemini-1.5-flash-001-tuning",
    CacheProps.CURRENT_MODEL.value: "models/gemini-exp-1206",
    CacheProps.CURRENT_PERSONA.value: "elara",
    CacheProps.CURRENT_PROMPTER.value: "grant"
}


@pytest.fixture
def cache_instance():
    """Provides a Cache instance with mocked file operations and injected data."""
    with patch("builtins.open", mock_open(read_data=json.dumps(TEST_CACHE_DATA))):
        cache = Cache("dummy_file.json")  # Filename is irrelevant now
        return cache


def test_cache_initialization(cache_instance):
    """Tests cache initialization and loading"""
    assert cache_instance.data == TEST_CACHE_DATA 


def test_cache_initialization_empty_data():
    """Tests initialization with no data."""
    with patch("builtins.open", mock_open(read_data="")):
        cache = Cache("dummy_file.json")
        assert cache.data == {
            CacheProps.CURRENT_MODEL.value: None,
            CacheProps.CURRENT_PERSONA.value: None,
            CacheProps.CURRENT_PROMPTER.value: None,
            CacheProps.MODELS.value: {
                CacheProps.MODELS_BASE.value: [],
                CacheProps.MODELS_TUNING.value: [],
                CacheProps.MODELS_TUNED.value: []
            },
            CacheProps.TUNING_MODEL.value: None,
        }


def test_cache_update(cache_instance):
    """Tests updating the cache."""
    new_model = "new_test_model"
    cache_instance.update(**{CacheProps.CURRENT_MODEL.value: new_model})
    assert cache_instance.get(CacheProps.CURRENT_MODEL.value) == new_model

    new_persona = "test_persona"
    cache_instance.update(**{CacheProps.CURRENT_PERSONA.value: new_persona})
    assert cache_instance.get(CacheProps.CURRENT_PERSONA.value) == new_persona

    cache_instance.update(**{"nonexistent_key": "some_value"})
    assert cache_instance.get("nonexistent_key") is None


def test_cache_save(cache_instance):
     """Tests saving the cache."""
     new_model = "another_test_model"
     cache_instance.update(**{CacheProps.CURRENT_MODEL.value: new_model})
     assert cache_instance.save()


def test_tuned_personas(cache_instance):
    """Tests retrieving tuned personas."""
    assert cache_instance.tuned_personas() == \
        TEST_CACHE_DATA[CacheProps.MODELS.value][CacheProps.MODELS_TUNED.value]


def test_is_tuned(cache_instance):
    """Tests checking if a persona is tuned."""
    assert not cache_instance.is_tuned("test_persona")