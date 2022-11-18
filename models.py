from typing import List

class Hour:
    from_: str
    to: str

class Monday:
    type: str
    hours: List[ Hour ]

class Tuesday:
    type: str
    hours: List[ Hour ]

class Wednesday:
    type: str
    hours: List[ Hour ]

class Thursday:
    type: str
    hours: List[ Hour ]

class Friday:
    type: str
    hours: List[ Hour ]

class Saturday:
    type: str
    hours: List[ Hour ]

class Successor:
    task_unique_id: int
    type: str
    lag: int

class Predecessor:
    task_unique_id: int
    type: str
    lag: int

class Assignment:
    start: str
    actual_work: int
    assignment_units: float
    work: int
    actual_start: str
    remaining_work: int
    unique_id: int
    task_unique_id: int
    regular_work: int
    percent_work_complete: float
    work_variance: int
    created: str
    guid: str
    resume: str
    stop: str
    rate_source: str
    finish: str
    actual_finish: str
    cost: float
    variable_rate_units: str
    resource_unique_id: int
    flag5: bool
    flag6: bool
    planned_work: int
    planned_start: str
    planned_finish: str

class CostRateTables:
    pass

class Recurrence:
    type: str
    start_date: str
    finish_date: str
    occurrences: int
    day_number: int
    month_number: int
    relative: bool
    weekly_days: List[ str ]

class Exception:
    name: str
    type: str
    recurrence: Recurrence
    from_: str
    to: str
    hours: List[ Hour ]

class Value:
    unique_id: int
    sequence_number: int
    name: str
    desription: str
    color: str

class ActivityCode:
    unique_id: int
    scope: str
    sequence_number: int
    name: str
    values: List[ Value ]
    scope_unique_id: int

class CustomProperties:
    CalculateFloatBasedOnFishDateOfEachProject: bool
    CalculateMultiplePathsUsingTotalFloat: bool
    CalendarForSchedulingRelationshipLag: str
    ComputeStartToStartLagFromEarlyStart: bool
    ComputeTotalFloatAs: str
    ConsiderAssignmentsInOtherProjectsWithPriorityEqualHigherThan: str
    IgnoreRelationshipsToAndFromOtherProjects: str
    LevelAllResources: bool
    LevelingPriorities: str
    LimitNumberOfPathsToCalculate: bool
    MaxPercentToOverallocateResources: str
    NumberofPathsToCalculate: str
    PreserveMinimumFloatWhenLeveling: str
    PreserveScheduledEarlyAndLateDates: bool
    UseExpectedFinishDates: bool
    WhenSchedulingProgressedActivitiesUseRetainedLogic: bool

class PropertyValues:
    start_date: str
    currency_symbol: str
    currency_symbol_position: str
    currency_digits: int
    thousands_separator: str
    decimal_separator: str
    default_work_units: str
    updating_task_status_updates_resource_status: bool
    date_order: str
    time_format: str
    default_start_time: str
    date_separator: str
    time_separator: str
    am_text: str
    pm_text: str
    date_format: str
    bar_text_date_format: str
    project_title: str
    default_calendar_unique_id: int
    schedule_from: str
    current_date: str
    default_end_time: str
    minutes_per_day: int
    days_per_month: int
    minutes_per_week: int
    minutes_per_month: int
    minutes_per_year: int
    default_task_earned_value_method: str
    new_tasks_estimated: bool
    auto_add_new_resources_and_tasks: bool
    last_saved: str
    auto_link: bool
    name: str
    default_task_type: str
    earned_value_method: str
    creation_date: str
    extended_creation_date: str
    default_fixed_cost_accrual: str
    fiscal_year_start_month: int
    new_task_start_is_project_start: bool
    new_tasks_are_manual: bool
    week_start_day: str
    currency_code: str
    mpx_delimiter: str
    mpx_program_name: str
    mpx_file_version: str
    mpx_code_page: str
    application_version: int
    file_application: str
    file_type: str
    guid: str
    critical_activity_type: str
    finish_date: str
    split_in_progress_tasks: bool
    microsoft_project_server_url: bool
    inserted_projects_like_summary: bool
    new_tasks_effort_driven: bool
    actuals_in_sync: bool
    company: str
    author: str
    honor_constraints: bool
    revision: int
    default_standard_rate: str
    default_overtime_rate: str
    status_date: str
    unique_id: int
    custom_properties: CustomProperties
    export_flag: bool
    project_id: str
    scheduled_finish: str
    planned_start: str

class Sunday:
    type: str
    hours: List[ Hour ]

class Calendar:
    unique_id: int
    name: str
    type: str
    sunday: Sunday
    monday: Monday
    tuesday: Tuesday
    wednesday: Wednesday
    thursday: Thursday
    friday: Friday
    saturday: Saturday
    parent_unique_id: int
    personal: bool
    exceptions: List[ Exception ]
    minutes_per_day: int
    minutes_per_week: int
    minutes_per_month: int
    minutes_per_year: int

class Resource:
    max_units: float
    accrue_at: str
    can_level: bool
    workgroup: str
    type: str
    created: str
    guid: str
    active: bool
    booking_type: str
    calendar_unique_id: int
    id: int
    name: str
    initials: str
    standard_rate: str
    cost: float
    work: int
    remaining_cost: float
    remaining_work: int
    work_variance: int
    cost_variance: float
    peak: float
    unique_id: int
    cost_rate_tables: CostRateTables
    overallocated: bool
    notes: str
    resource_id: str
    parent_id: int

class Task:
    start: str
    leveling_delay_units: str
    name: str
    wbs: str
    constraint_type: str
    critical: bool
    priority: int
    actual_duration: int
    duration: int
    remaining_duration: int
    percent_complete: float
    early_start: str
    early_finish: str
    late_start: str
    late_finish: str
    actual_start: str
    unique_id: int
    summary: bool
    created: str
    resume: str
    stop: str
    outline_number: str
    type: str
    fixed_cost_accrual: str
    leveling_can_split: bool
    level_assignments: bool
    complete_through: str
    guid: str
    active: bool
    finish: str
    id: int
    outline_level: int
    parent_task_unique_id: int
    calendar_unique_id: int
    free_slack: int
    total_slack: int
    successors: List[ Successor ]
    finish_slack: int
    predecessors: List[ Predecessor ]
    percent_work_complete: float
    actual_finish: str
    milestone: bool
    actual_duration_units: str
    work: int
    remaining_work: int
    cost: float
    duration_variance: int
    effort_driven: bool
    constraint_date: str
    start_slack: int
    overallocated: bool
    rollup: bool
    text1: str
    baseline_work: int
    baseline_duration: int
    remaining_early_start: str
    remaining_early_finish: str
    remaining_late_start: str
    remaining_late_finish: str
    baseline_start: str
    baseline_finish: str
    project: str
    planned_finish: str
    planned_start: str
    planned_duration: int
    planned_work: int
    activity_id: str
    percent_complete_type: str
    ignore_resource_calendar: bool
    activity_status: str
    activity_type: str
    activity_codes: List[ int ]
    longest_path: bool
    primary_resource_id: int

class Project:
    custom_fields: List[ None ]
    property_values: PropertyValues
    calendars: List[ Calendar ]
    resources: List[ Resource ]
    tasks: List[ Task ]
    assignments: List[ Assignment ]
    activity_codes: List[ ActivityCode ]