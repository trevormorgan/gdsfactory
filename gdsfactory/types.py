from gdsfactory.config import logger
from gdsfactory.typings import (
    Callable,
    Component,
    ComponentFactory,
    ComponentFactoryDict,
    ComponentSpec,
    ComponentOrPath,
    ComponentOrReference,
    Coordinate,
    Coordinates,
    CrossSection,
    CrossSectionFactory,
    CrossSectionOrFactory,
    CrossSectionSpec,
    MultiCrossSectionAngleSpec,
    Float2,
    Float3,
    Floats,
    Int2,
    Int3,
    Ints,
    Layer,
    Label,
    Layers,
    LayerLevel,
    LayerStack,
    LayerSpec,
    LayerSpecs,
    NameToFunctionDict,
    Number,
    PathType,
    PathTypes,
    Route,
    RouteFactory,
    Routes,
    Strs,
    Section,
    Any,
    Dict,
    List,
    Optional,
    Union,
    Tuple,
)


logger.warning(
    "gdsfactory.types has been renamed to gdsfactory.typings. types will be removed in the near future.",
    DeprecationWarning,
)

__all__ = (
    "Callable",
    "Component",
    "ComponentFactory",
    "ComponentFactoryDict",
    "ComponentSpec",
    "ComponentOrPath",
    "ComponentOrReference",
    "Coordinate",
    "Coordinates",
    "CrossSection",
    "CrossSectionFactory",
    "CrossSectionOrFactory",
    "CrossSectionSpec",
    "MultiCrossSectionAngleSpec",
    "Float2",
    "Float3",
    "Floats",
    "Int2",
    "Int3",
    "Ints",
    "Layer",
    "Label",
    "Layers",
    "LayerLevel",
    "LayerStack",
    "LayerSpec",
    "LayerSpecs",
    "NameToFunctionDict",
    "Number",
    "PathType",
    "PathTypes",
    "Route",
    "RouteFactory",
    "Routes",
    "Strs",
    "Section",
    "Any",
    "Dict",
    "List",
    "Optional",
    "Union",
    "Tuple",
)
