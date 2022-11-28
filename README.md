# Python CLI Interaction Library

## Introduction

This library is created for simplify `INPUT`/`OUTPUT` procedure when generating `YAML`/`JSON` configurations for daemon services.

## Get Started

`TODO: complete this example`

You can follow this example.

```python
resolution_sel = must_parse_cli_sel("Select color resolution", self.__COLOR_RESOLUTION_CANDIDATES__,
                                                default_value=self.__COLOR_RESOLUTION_DEFAULT_SEL__)
fps_sel = must_parse_cli_sel("Select color fps", self.__COLOR_FPS_CANDIDATES__, default_value=self.__COLOR_FPS_DEFAULT_SEL__)
format_sel = must_parse_cli_sel("Select color format", self.__COLOR_FORMAT_CANDIDATES__,
                                            default_value=self.__COLOR_FORMAT_DEFAULT_SEL__)
exposure_sel = must_parse_cli_int("Set exposure [ 0 - 10000 ], -1 for auto exposure", min=-1, max=10001, default_value=-1)
```
