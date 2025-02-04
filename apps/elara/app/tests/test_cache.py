import json
from unittest.mock import patch, mock_open

import pytest

from objects.cache import Cache
import properties  # Assuming this is where CacheProps and ModelProps are defined

# Sample Cache Data for testing (no longer needs to be in a file)
TEST_CACHE_DATA = {
    properties.CacheProps.CURRENT_MODEL.value: "test_model",
    properties.CacheProps.CURRENT_PERSONA.value: "test_persona",
    properties.CacheProps.CURRENT_PROMPTER.value: "test_prompter",
    properties.CacheProps.MODELS.value: ["model1", "model2"],
    properties.CacheProps.TUNING_MODEL.value: "test_tuning_model",
    properties.ModelProps.NAME.value: "test_name"
}

@pytest.fixture
def cache_instance():
    """Provides a Cache instance with mocked file operations and injected data."""
    with patch("builtins.open", mock_open(read_data=json.dumps(TEST_CACHE_DATA))) as mock_file:
        cache = Cache("dummy_file.json")  # Filename is irrelevant now
        return cache


def test_cache_initialization(cache_instance):
    """Tests cache initialization and loading"""
    assert cache_instance.data == TEST_CACHE_DATA 


def test_cache_initialization_empty_data():
    """Tests initialization with no data."""
    with patch("builtins.open", mock_open(read_data="")) as mock_file:
        cache = Cache("dummy_file.json")
        assert cache.data == {
            properties.CacheProps.CURRENT_MODEL.value: None,
            properties.CacheProps.CURRENT_PERSONA.value: None,
            properties.CacheProps.CURRENT_PROMPTER.value: None,
            properties.CacheProps.MODELS.value: [],
            properties.CacheProps.TUNING_MODEL.value: None,
        }


def test_cache_update(cache_instance):
    """Tests updating the cache."""
    new_model = "new_test_model"
    cache_instance.update(**{properties.CacheProps.CURRENT_MODEL.value: new_model})
    assert cache_instance.get(properties.CacheProps.CURRENT_MODEL.value) == new_model

    new_models = ["model3","model4"]
    cache_instance.update(**{properties.CacheProps.MODELS.value: new_models})
    assert cache_instance.get(properties.CacheProps.MODELS.value) == ["model1", "model2", "model3", "model4"]

    cache_instance.update(**{"nonexistent_key": "some_value"})
    assert cache_instance.get("nonexistent_key") is None


def test_cache_save(cache_instance):
     """Tests saving the cache."""
     new_model = "another_test_model"
     cache_instance.update(**{properties.CacheProps.CURRENT_MODEL.value: new_model})
     assert cache_instance.save()


def test_cache_save_error(cache_instance):
    """Tests the scenario when the cache can't be saved."""
    with patch("builtins.open", mock_open(), side_effect=Exception("Save error")):
        assert not cache_instance.save()


def test_tuned_personas(cache_instance):
    """Tests retrieving tuned personas."""
    assert cache_instance.tuned_personas() == []


def test_is_tuned(cache_instance):
    """Tests checking if a persona is tuned."""
    assert not cache_instance.is_tuned("test_persona")