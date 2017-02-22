import json

class BaseDataType(object):

    def __init__(self, model=None):
        self.datatype_model = model

    def validate(self, value, source=None):
        return []

    def append_to_document(self, document, nodevalue):
        """
        Assigns a given node value to the corresponding key in a document in
        in preparation to index the document
        """
        pass

    def transform_import_values(self, value):
        """
        Transforms values from probably string/wkt representation to specified
        datatype in arches
        """
        return value

    def transform_export_values(self, value):
        """
        Transforms values from probably string/wkt representation to specified
        datatype in arches
        """
        return value

    def get_bounds(self, tile, node):
        """
        Gets the bounds of a geometry if the datatype is spatial
        """
        return None

    def get_layer_config(self, node=None):
        """
        Gets the layer config to generate a map layer (use if spatial)
        """
        return None

    def get_map_layer(self, node=None):
        """
        Gets the array of map layers to add to the map for a given node
        should be a dictionary including (as in map_layers table):
        nodeid, name, layerdefinitions, isoverlay, icon
        """
        return None

    def get_map_source(self, node=None, preview=False):
        """
        Gets the map source definition to add to the map for a given node
        should be a dictionary including (as in map_sources table):
        name, source (json)
        """
        if node is None:
            return None
        source_config = {
            "type": "vector",
            "tiles": ["/tileserver/%s/{z}/{x}/{y}.pbf" % node.nodeid]
        }
        if preview:
            source_config = {
                "type": "geojson",
                "data": {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "properties": {
                                "total": 1
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -122.4810791015625,
                                    37.93553306183642
                                ]
                            }
                        },
                        {
                            "type": "Feature",
                            "properties": {
                                "total": 100
                            },
                            "geometry": {
                                "type": "Point",
                                "coordinates": [
                                    -118.30078125,
                                    34.075412438417395
                                ]
                            }
                        },
                        {
                            "type": "Feature",
                            "properties": {
                                "total": 1
                            },
                            "geometry": {
                                "type": "LineString",
                                "coordinates": [
                                    [
                                        -179.82421875,
                                        44.213709909702054
                                    ],
                                    [
                                        -154.16015625,
                                        32.69486597787505
                                    ],
                                    [
                                        -171.5625,
                                        18.812717856407776
                                    ],
                                    [
                                        -145.72265625,
                                        2.986927393334876
                                    ],
                                    [
                                        -158.37890625,
                                        -30.145127183376115
                                    ]
                                ]
                            }
                        },
                        {
                            "type": "Feature",
                            "properties": {
                                "total": 1
                            },
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [
                                            -50.9765625,
                                            22.59372606392931
                                        ],
                                        [
                                            -23.37890625,
                                            22.59372606392931
                                        ],
                                        [
                                            -23.37890625,
                                            42.94033923363181
                                        ],
                                        [
                                            -50.9765625,
                                            42.94033923363181
                                        ],
                                        [
                                            -50.9765625,
                                            22.59372606392931
                                        ]
                                    ]
                                ]
                            }
                        },
                        {
                            "type": "Feature",
                            "properties": {
                                "total": 1
                            },
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [
                                    [
                                        [
                                            -27.59765625,
                                            -14.434680215297268
                                        ],
                                        [
                                            -24.43359375,
                                            -32.10118973232094
                                        ],
                                        [
                                            0.87890625,
                                            -31.653381399663985
                                        ],
                                        [
                                            2.28515625,
                                            -12.554563528593656
                                        ],
                                        [
                                            -14.23828125,
                                            -0.3515602939922709
                                        ],
                                        [
                                            -27.59765625,
                                            -14.434680215297268
                                        ]
                                    ]
                                ]
                            }
                        }
                    ]
                }
            }
        return {
            "nodeid": node.nodeid,
            "name": "resources-%s" % node.nodeid,
            "source": json.dumps(source_config)
        }

    def get_pref_label(self, nodevalue):
        """
        Gets the prefLabel of a concept value
        """
        return None

    def get_display_value(self, tile, node):
        """
        Returns a list of concept values for a given node
        """
        return None

    def get_search_term(self, nodevalue):
        """
        Returns a nodevalue if it qualifies as a search term
        """
        return None

    def manage_files(self, previously_saved_tile, current_tile, request, node):
        """
        Updates files
        """
        pass
