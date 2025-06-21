.. MODE: OVERRIDE
..
.. This document contains a collection of poetry and my resume. This comment contains a solitication from a journal and some context surrounding the journal. The goal is to find the most likely poems to be published in the given solicitation. Use the context to create a taste profile of the journal. Select poems from the collection below that meet the this profile. If there are none, say so. If a submission is possible, create a cover for the letter submission and any other additional material (biography, etc) the solitication requires for submission.
..
.. The collection also contains submission histories. Use this data to influence your decision, i.e. take into account the number of rejections and allow it to update your posterior probabilities about the likelihood of getting published. 
..
..
.. # SOLICITATION: {{ solicitation.title }}
.. 
.. {{ solitation.body }}
..
.. # RANDOM POEMS FROM THEIR ISSUES
.. 
{% for ex in solitication.taste_profile.examples %}
.. {{ ex }}
{% endfor %}