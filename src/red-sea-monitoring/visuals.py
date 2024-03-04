from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import Legend, Span, Label
from bokeh.layouts import column
from bokeh.core.validation import silence
from bokeh.core.validation.warnings import EMPTY_LAYOUT


# Use the silence function to ignore the EMPTY_LAYOUT warning
silence(EMPTY_LAYOUT, True)


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

    sub_title_fig = figure(title=source, toolbar_location=None, width=750, height=40)
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
    measure = 'nrEvents'
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
