select
    region_id,
    user_id,
    client_version,
    event_type,
    event_data,
    event_timestamp,
    event_id,
    received_at,
    '{{ run_started_at }}' :: timestamp as dbt_run_started_at
from {{ source('landing_tables', 'user_events') }}
