---
title: "switch"
status: realm-server-client
---

[Back to Shared](index.md)

<a id="switch"></a>
# `switch` { .api-method-title }

=== "Server"

    <div class="api-badges"><span class="api-badge api-badge--server">server</span></div>

    <div class="api-signature" markdown>

    ```lua
    function switch(case, cases)
    ```

    </div>

    Switch statement implementation for Lua.

    ## Example { #server-example data-toc-label="Example" }

    ```lua
    switch(self._guardType, {
    	["sude"] = function()
    		return "ladsource/y0/guard_sude/default_sude"..math.random(1,2)..".wav"
    	end,
    	["metal"] = function()
    		return "ladsource/y0/guard_sude/metal"..math.random(1,2)..".wav"
    	end,
    	["katana"] = function()
    		self:VFX_HandSpark()
    		return "ladsource/y0/guard_sude/katana"..math.random(1,2)..".wav"
    	end,
    	["bokuto"] = function()
    		return "ladsource/y0/guard_default/bokuto_default"..math.random(1,2)..".wav"
    	end,
    	["bullet"] = function()
    		self:VFX_HandSpark()
    		return "ladsource/y0/guard_sude/bullet"..math.random(1,2)..".wav"
    	end,
    	default = function()
    		return "ladsource/y0/guard_sude/default_sude"..math.random(1,2)..".wav"
    	end
    })
    ```

    ## Parameters { #server-parameters data-toc-label="Parameters" }

    <div class="api-parameter-table" markdown>

    | Name | Type | Required | Description |
    | --- | --- | :---: | --- |
    | `case` | `any` | Yes | The value to match against the cases. |
    | `cases` | `table` | Yes | A table of case values and corresponding functions. The keys are the case values, and the values are functions to execute for each case. |

    </div>

    ## Returns { #server-returns data-toc-label="Returns" }

    | Type | Description |
    | --- | --- |
    | `any` | The return value of the executed function, or nil if no match is found and no default function is provided. |

    <p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1369</code>.</p>

=== "Client"

    <div class="api-badges"><span class="api-badge api-badge--client">client</span></div>

    <div class="api-signature" markdown>

    ```lua
    function switch(case, cases)
    ```

    </div>

    Client-side implementation of the Lua switch statement helper.

    ## Parameters { #client-parameters data-toc-label="Parameters" }

    <div class="api-parameter-table" markdown>

    | Name | Type | Required | Description |
    | --- | --- | :---: | --- |
    | `case` | `any` | Yes | The value to match against the cases. |
    | `cases` | `table` | Yes | A table of case values and corresponding functions. |

    </div>

    ## Returns { #client-returns data-toc-label="Returns" }

    | Type | Description |
    | --- | --- |
    | `any` | The return value of the executed function, or nil if no matching or default case exists. |

    <p class="api-source">Defined in <code>lua/entities/lad_framework_base/shared.lua:1577</code>.</p>
