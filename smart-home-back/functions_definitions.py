


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "turn_on_lamp",
            "description": "Turns on a lamp in a specific location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["kitchen", "bathroom", "room 1", "room 2"],
                        "description": "The specific location of the lamp to turn on."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "turn_off_lamp",
            "description": "Turns off a lamp in a specific location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["kitchen", "bathroom", "room 1", "room 2"],
                        "description": "The specific location of the lamp to turn off."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_lamp_status",
            "description": "Gets the current status (ON/OFF) of a lamp in a specific location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["kitchen", "bathroom", "room 1", "room 2"],
                        "description": "The specific location of the lamp to get status."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "turn_on_ac",
            "description": "Turns on an AC unit in a specific location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["room 1", "kitchen"],
                        "description": "The specific location of the AC unit to turn on."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "turn_off_ac",
            "description": "Turns off an AC unit in a specific location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["room 1", "kitchen"],
                        "description": "The specific location of the AC unit to turn off."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "set_ac_temperature",
            "description": "Sets the temperature of an AC unit in a specific location. Temperature range is 18-30 degrees Celsius.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["room 1", "kitchen"],
                        "description": "The specific location of the AC unit."
                    },
                    "temperature": {
                        "type": "integer",
                        "minimum": 18,
                        "maximum": 30,
                        "description": "The desired temperature in degrees Celsius (e.g., 22)."
                    }
                },
                "required": ["location", "temperature"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_ac_status",
            "description": "Gets the current status (ON/OFF and temperature) of an AC unit in a specific location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["room 1", "kitchen"],
                        "description": "The specific location of the AC unit to get status."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_ac_temperature",
            "description": "Gets the current set temperature of an AC unit in a specific location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["room 1", "kitchen"],
                        "description": "The specific location of the AC unit to get temperature."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "turn_on_tv",
            "description": "Turns on the television in the living room.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["living room"],
                        "description": "The location of the TV (must be 'living room')."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "turn_off_tv",
            "description": "Turns off the television in the living room.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["living room"],
                        "description": "The location of the TV (must be 'living room')."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "change_tv_channel",
            "description": "Changes the channel of the television in the living room. Channel range is 1-100.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["living room"],
                        "description": "The location of the TV (must be 'living room')."
                    },
                    "channel": {
                        "type": "integer",
                        "minimum": 1,
                        "maximum": 100,
                        "description": "The desired channel number (e.g., 5)."
                    }
                },
                "required": ["location", "channel"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "mute_tv",
            "description": "Mutes the television in the living room.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["living room"],
                        "description": "The location of the TV (must be 'living room')."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "unmute_tv",
            "description": "Unmutes the television in the living room.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["living room"],
                        "description": "The location of the TV (must be 'living room')."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_tv_status",
            "description": "Gets the current status (ON/OFF, channel, muted) of the television in the living room.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["living room"],
                        "description": "The location of the TV (must be 'living room')."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_tv_channel",
            "description": "Gets the current channel of the television in the living room.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "enum": ["living room"],
                        "description": "The location of the TV (must be 'living room')."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Retrieves the current weather conditions for a specified city. Example: 'What's the weather in Tehran?'",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The name of the city (e.g., 'Tehran', 'London')."
                    }
                },
                "required": ["location"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_latest_news",
            "description": "Retrieves the latest news articles based on a query. Can specify a topic or keyword. Example: 'Tell me about the latest news on AI' or 'What's the news about Iran in Persian?'",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The topic or keyword for the news search (e.g., 'technology', 'sports', 'Iran'). Default is 'general'."
                    },
                    "language": {
                        "type": "string",
                        "enum": ["ar", "de", "en", "es", "fr", "he", "it", "nl", "no", "pt", "ru", "sv", "zh", "fa"], # Added 'fa' for Persian
                        "description": "The language of the news. Default is 'en' (English). Examples: 'en' for English, 'fa' for Persian."
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_date_time",
            "description": "Returns the current date and time. Example: 'What time is it?' or 'What's the date today?'",
            "parameters": {
                "type": "object",
                "properties": {}, 
                "required": []
            }
        }
    }

]