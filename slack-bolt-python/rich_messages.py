initial_troubleshooting_block=[
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Troubleshooting options",
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "radio_buttons",
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Restart AEM (In development)",
                                "emoji": True
                            },
                            "value": "value-0"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Systemcheck",
                                "emoji": True
                            },
                            "value": "value-1"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Clear Cache (In development)",
                                "emoji": True
                            },
                            "value": "value-2"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Create Trouble Ticket (In development)",
                                "emoji": True
                            },
                            "value": "value-3"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Snapshot Recovery (In development)",
                                "emoji": True
                            },
                            "value": "value-4"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Others (In development)",
                                "emoji": True
                            },
                            "value": "value-5"
                        }],
                    "action_id": "radio-actions"
                        }
            ]
        }
        ]
systemcheck_block=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "systemcheck"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname(Systemcheck)",
                       }
                    }
                    ]

restart_aem_block=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "restart-aem"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname(Restart AEM)",
                       }
                    }
                    ]
clear_cache_block=[
                    {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "static_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select app",
                                "emoji": True
                            },
                            "options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "CC",
                                        "emoji": True
                                    },
                                    "value": "value-0"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "APP",
                                        "emoji": True
                                    },
                                    "value": "value-1"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Helpx",
                                        "emoji": True
                                    },
                                    "value": "value-2"
                                }
                            ],
                            "action_id": "application"
                        },
                        {
                            "type": "static_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select environment",
                                "emoji": True
                            },
                            "options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "dev",
                                        "emoji": True
                                    },
                                    "value": "value-0"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "QA",
                                        "emoji": True
                                    },
                                    "value": "value-1"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Stage",
                                        "emoji": True
                                    },
                                    "value": "value-2"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Prod",
                                        "emoji": True
                                    },
                                    "value": "value-3"
                                }
                            ],
                            "action_id": "environment"
                        }
                        ]}]
snapshot_recovery_block=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "snapshot-recovery"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname(Snapshot Recovery)",
                       }
                    }
                    ]
create_trouble_ticket_block=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "create-trouble-ticket"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname(Create Trouble Ticket)",
                       }
                    }
                    ]
others_block=[
                    {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Pick an action from the dropdown list"
                    },
                    "accessory": {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select an item",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Put into service (In development)",
                                    "emoji": True
                                },
                                "value": "value-0"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Take out of service (In development)",
                                    "emoji": True
                                },
                                "value": "value-1"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Check bundles (In development)",
                                    "emoji": True
                                },
                                "value": "value-2"
                            }
                            ],
                            "action_id": "static_select-action"
                        }}]
unauthorized_block=[
                {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "unauthorized",
                }}]
put_in_service_block=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "put-in-service"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname(Put into service)",
                       }
                    }
                    ]
take_out_of_service_block=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "take-out-of-service"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname(Take out of service)",
                       }
                    }
                    ]
check_bundles_block=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "check-bundles"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname(Check bundles)",
                       }
                    }
                    ]
cant_find_server_block=[
                {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Can't find server"
                }}]
initiate_new_conversation_block=[
            {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Please initiate a new conversation with Bot!!",
            }}]
restricted_to_ops=[
                        {
                        "type": "section",
                        "text": {
                            "type": "plain_text",
                            "text": "This operation is only permitted by members of WCMS-OPS team"
                        }}]
take_outof_service_action=[
        {
         "type": "section",
         "text": {
            "type": "plain_text",
            "text": "Take out of service is still WIP. Please check back later",
        }}]
