import datetime
import pandas as pd

from bokeh.core.validation import silence
from bokeh.core.validation.warnings import EMPTY_LAYOUT
from bokeh.layouts import column
from bokeh.models import HoverTool, Label, Legend, Span, Title
from bokeh.plotting import ColumnDataSource, figure

# Use the silence function to ignore the EMPTY_LAYOUT warning
silence(EMPTY_LAYOUT, True)

COLORS = [
    "#4E79A7",  # Blue
    "#F28E2B",  # Orange
    "#E15759",  # Red
    "#76B7B2",  # Teal
    "#59A14F",  # Green
    "#EDC948",  # Yellow
    "#B07AA1",  # Purple
    "#FF9DA7",  # Pink
    "#9C755F",  # Brown
    "#BAB0AC",  # Gray
    "#7C7C7C",  # Dark gray
    "#6B4C9A",  # Violet
    "#D55E00",  # Orange-red
    "#CC61B0",  # Magenta
    "#0072B2",  # Bright blue
    "#329262",  # Peacock green
    "#9E5B5A",  # Brick red
    "#636363",  # Medium gray
    "#CD9C00",  # Gold
    "#5D69B1",  # Medium blue
]


def get_bar_chart(
    dataframe,
    title,
    source,
    subtitle=None,
    measure="measure",
    category="category",
    color_code=None,
    category_value=None,
    crisis_date=None,
    conflict_date=None,
):
    # Initialize the figure
    p2 = figure(x_axis_type="datetime", width=750, height=400, toolbar_location="above")
    p2.add_layout(Legend(), "right")

    # Define the color palette (make sure this has enough colors for the categories)
    color_palette = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

    # Loop through each unique category and plot a bar
    # for id, unique_category in enumerate(dataframe[category].unique()):
    # Filter the DataFrame for each category
    category_df = dataframe[dataframe[category] == category_value].copy()
    category_df.sort_values(
        by="event_date", inplace=True
    )  # Ensure the DataFrame is sorted by date
    category_source = ColumnDataSource(category_df)

    # Plot the bars
    p2.vbar(
        x="event_date",
        top=measure,
        width=86400000 * 1.5,
        source=category_source,
        color=color_code,
    )

    # Configure legend
    p2.legend.click_policy = "hide"
    p2.legend.location = "top_right"

    # Set the subtitle as the title of the plot if it exists
    if subtitle:
        p2.title.text = subtitle

    # Create title and subtitle text using separate figures
    title_fig = figure(title=title, toolbar_location=None, width=750, height=40)
    title_fig.title.align = "left"
    title_fig.title.text_font_size = "14pt"
    title_fig.border_fill_alpha = 0
    title_fig.outline_line_color = None

    sub_title_fig = figure(title=source, toolbar_location=None, width=750, height=80)
    sub_title_fig.title.align = "left"
    sub_title_fig.title.text_font_size = "10pt"
    sub_title_fig.title.text_font_style = "normal"
    sub_title_fig.border_fill_alpha = 0
    sub_title_fig.outline_line_color = None

    p2.renderers.extend(
        [
            Span(
                location=crisis_date,
                dimension="height",
                line_color="#7C7C7C",
                line_width=2,
                line_dash=(4, 4),
            ),
            Span(
                location=conflict_date,
                dimension="height",
                line_color="#7C7C7C",
                line_width=2,
                line_dash=(4, 4),
            ),
        ]
    )

    crisis_label = Label(
        y=250,  # Adjust as needed
        x=crisis_date,
        y_units="screen",
        text="Red Sea Crisis",
        render_mode="css",
        background_fill_color="white",
        background_fill_alpha=0.7,
        text_font_size="9pt",
    )

    conflict_label = Label(
        y=290,  # Adjust as needed
        x=conflict_date,
        y_units="screen",
        text="Middle East Conflict",
        render_mode="css",
        background_fill_color="white",
        background_fill_alpha=0.7,
        text_font_size="9pt",
    )

    p2.add_layout(crisis_label)
    p2.add_layout(conflict_label)

    # Combine the title, plot, and subtitle into a single layout
    layout = column(title_fig, p2, sub_title_fig)

    return layout


def get_stacked_bar_chart(
    dataframe,
    title,
    source,
    subtitle=None,
    date_column="date",
    categories=None,
    colors=None,
    crisis_date=None,
    conflict_date=None,
    category_column="event_type",
    measure="nrEvents",
):
    df_pivot = dataframe.pivot_table(
        index=date_column, columns=category_column, values=measure, fill_value=0
    ).reset_index()
    # Ensure that the dataframe has all the necessary categories
    # for category in categories:
    #     if category not in df_pivot.columns:
    #         df_pivot[category] = 0  # Add missing categories with 0 values

    # Initialize the figure
    p2 = figure(x_axis_type="datetime", width=750, height=400, toolbar_location="above")

    # Convert dataframe to ColumnDataSource
    source = ColumnDataSource(df_pivot)

    p2 = figure(
        x_axis_type="datetime",
        width=750,
        height=400,
        title=title,
        toolbar_location="above",
    )

    # Stack bars
    renderers = p2.vbar_stack(
        stackers=categories,
        x=date_column,
        width=86400000 * 3,
        color=colors,
        source=source,
    )

    legend = Legend(
        items=[
            (category, [renderer]) for category, renderer in zip(categories, renderers)
        ],
        location=(0, -30),
    )
    p2.add_layout(legend, "right")

    # Configure legend
    p2.legend.click_policy = "hide"
    p2.legend.location = "top_right"

    # Add crisis and conflict lines if dates are provided
    if crisis_date:
        p2.add_layout(
            Span(
                location=crisis_date,
                dimension="height",
                line_color="#7C7C7C",
                line_width=2,
                line_dash=(4, 4),
            )
        )
    if conflict_date:
        p2.add_layout(
            Span(
                location=conflict_date,
                dimension="height",
                line_color="#7C7C7C",
                line_width=2,
                line_dash=(4, 4),
            )
        )

    crisis_label = Label(
        y=250,  # Adjust as needed
        x=crisis_date,
        y_units="screen",
        text="Red Sea Crisis",
        render_mode="css",
        background_fill_color="white",
        background_fill_alpha=0.7,
        text_font_size="9pt",
    )

    conflict_label = Label(
        y=290,  # Adjust as needed
        x=conflict_date,
        y_units="screen",
        text="Middle East Conflict",
        render_mode="css",
        background_fill_color="white",
        background_fill_alpha=0.7,
        text_font_size="9pt",
    )

    p2.add_layout(crisis_label)
    p2.add_layout(conflict_label)

    # # Set subtitles and titles
    # title_fig = _create_title_figure(title, width=750, height=50, font_size="14pt")
    # sub_title_fig = _create_title_figure(subtitle if subtitle else source, width=750, height=30, font_size="10pt", font_style="normal")

    # Combine everything into a single layout
    layout = column(p2)

    return layout


def _create_title_figure(text, width, height, font_size, font_style="bold"):
    title_fig = figure(toolbar_location=None, width=width, height=height)
    title_fig.title.text = text
    title_fig.title.align = "left"
    title_fig.title.text_font_size = font_size
    title_fig.title.text_font_style = font_style
    title_fig.grid.grid_line_color = None
    title_fig.axis.axis_line_color = None
    title_fig.axis.major_label_text_color = None
    title_fig.axis.major_tick_line_color = None
    title_fig.axis.minor_tick_line_color = None
    title_fig.outline_line_color = None
    return title_fig


def plot_visits(data: pd.DataFrame, title="Points of Interest Visit Trends"):
    """Plot Points of Interest Visit Time Series

    Attributes
    ----------
    bearer: pd.DataFrame
        Time Series pivot table each column representing a line

    title: str
        Plot title
    """

    p = figure(
        title=title,
        width=750,
        height=750,
        x_axis_label="Date",
        x_axis_type="datetime",
        y_axis_label="Count of Devices",
        y_axis_type="log",
        y_range=(0.75, 5 * 10**3),
        tools="pan,reset,save,box_select",
    )
    p.add_layout(Legend(), "right")
    p.add_layout(
        Title(
            text="Count of Devices Identified with OpenStreetMap tag",
            text_font_size="12pt",
            text_font_style="italic",
        ),
        "above",
    )
    p.add_layout(
        Title(
            text=f"Source: Veraset Movement. Creation date: {datetime.datetime.today().strftime('%d %B %Y')}. Feedback: datalab@worldbank.org.",
            text_font_size="10pt",
            text_font_style="italic",
        ),
        "below",
    )

    # plot spans
    p.renderers.extend(
        [
            Span(
                location=datetime.datetime(2023, 10, 7),
                dimension="height",
                line_color="grey",
                line_width=2,
                line_dash=(4, 4),
            ),
            Span(
                location=datetime.datetime(2023, 11, 17),
                dimension="height",
                line_color="grey",
                line_width=2,
                line_dash=(4, 4),
            ),
        ]
    )

    # plot lines
    for i, (col, color) in enumerate(zip(data.columns, COLORS)):
        try:
            r = p.line(
                data.index,
                data[col],
                legend_label=col,
                line_color=color,
                line_width=2,
            )
            if i != 0:
                r.muted = True
        except KeyError:
            pass

    p.add_tools(
        HoverTool(
            tooltips=[("Date", "@x{%F}"), ("Count", "@y")],
            formatters={"@x": "datetime"},
        )
    )

    p.legend.location = "bottom_left"
    p.legend.click_policy = "mute"
    p.title.text_font_size = "16pt"
    p.sizing_mode = "scale_both"
    return p
