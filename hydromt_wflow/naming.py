"""Mapping dictionaries from hydromt to hydromt_wflow to Wflow.jl names."""

HYDROMT_NAMES = {
    "flwdir": "wflow_ldd",
    "elevtn": "wflow_dem",
    "subelv": "dem_subgrid",
    "uparea": "wflow_uparea",
    "strord": "wflow_streamorder",
    "basins": "wflow_subcatch",
    "rivlen": "wflow_riverlength",
    "rivmsk": "wflow_river",
    "rivwth": "wflow_riverwidth",
    "lndslp": "Slope",
    "rivslp": "RiverSlope",
    "rivdph": "RiverDepth",
    "rivman": "N_River",
    "gauges": "wflow_gauges",
    "landuse": "wflow_landuse",
    "soil": "wflow_soil",
    "resareas": "wflow_reservoirareas",
    "reslocs": "wflow_reservoirlocs",
    "lakeareas": "wflow_lakeareas",
    "lakelocs": "wflow_lakelocs",
    "glacareas": "wflow_glacierareas",
    "glacfracs": "wflow_glacierfrac",
    "glacstore": "wflow_glacierstore",
    "dom_gross": "domestic_gross",
    "dom_net": "domestic_net",
    "ind_gross": "industry_gross",
    "ind_net": "industry_net",
    "lsk_gross": "livestock_gross",
    "lsk_net": "livestock_net",
}


WFLOW_NAMES = {
    "landuse": None,
    "Kext": "input.vertical.kext",
    "N": "input.lateral.land.n",
    "PathFrac": "input.vertical.pathfrac",
    "RootingDepth": "input.vertical.rootingdepth",
    "Sl": "input.vertical.specific_leaf",
    "Swood": "input.vertical.storage_wood",
    "WaterFrac": "input.vertical.waterfrac",
    "kc": "input.vertical.kc",
    "alpha_h1": "input.vertical.alpha_h1",
    "h1": "input.vertical.h1",
    "h2": "input.vertical.h2",
    "h3_high": "input.vertical.h3_high",
    "h3_low": "input.vertical.h3_low",
    "h4": "input.vertical.h4",
}

WFLOW_SEDIMENT_NAMES = {
    "landuse": None,
    "Kext": "input.vertical.kext",
    "PathFrac": "input.vertical.pathfrac",
    "Sl": "input.vertical.specific_leaf",
    "Swood": "input.vertical.storage_wood",
    "USLE_C": "input.vertical.usleC",
}