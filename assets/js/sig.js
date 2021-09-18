---
---
{% assign latest_year = site.posts | group_by: "year" | map: "name" | sort | last %}

$(document).ready(function() {
    let url = new URL(window.location.href);
    let year = url.searchParams.get("year");

    if ($(`#${year}-projects-tab`)[0])
        $(`#${year}-projects-tab`).click();
    else
        $("#{{latest_year}}-projects-tab").click();
});