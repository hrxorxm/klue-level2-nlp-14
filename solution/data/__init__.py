from .collator import (
    DefaultDataCollator
)
from .entity_tagging import mark_entity_spans, convert_example_to_features

COLLATOR_MAP = {
    "default": DefaultDataCollator
}