from __future__ import annotations
from datetime import datetime, date
from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel as BaseModel, Field
from linkml_runtime.linkml_model import Decimal
import sys
if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


metamodel_version = "None"
version = "None"

class WeakRefShimBaseModel(BaseModel):
   __slots__ = '__weakref__'

class ConfiguredBaseModel(WeakRefShimBaseModel,
                validate_assignment = True,
                validate_all = True,
                underscore_attrs_are_private = True,
                extra = 'forbid',
                arbitrary_types_allowed = True,
                use_enum_values = True):
    pass


class InteractionCollection(ConfiguredBaseModel):
    
    interactions: Optional[List[Interaction]] = Field(default_factory=list)
    


class Interaction(ConfiguredBaseModel):
    
    subject: Optional[str] = Field(None)
    subject_activity: Optional[str] = Field(None)
    subject_location: Optional[str] = Field(None)
    subject_process: Optional[str] = Field(None)
    relation: Optional[str] = Field(None)
    object: Optional[str] = Field(None)
    object_activity: Optional[str] = Field(None)
    object_location: Optional[str] = Field(None)
    object_process: Optional[str] = Field(None)
    model: Optional[str] = Field(None)
    state: Optional[str] = Field(None)
    



# Update forward refs
# see https://pydantic-docs.helpmanual.io/usage/postponed_annotations/
InteractionCollection.update_forward_refs()
Interaction.update_forward_refs()

