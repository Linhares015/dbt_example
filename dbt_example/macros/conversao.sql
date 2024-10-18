{% macro to_snake_case(string) %}
    {{ string | lower | replace(' ', '_') }}
{% endmacro %}