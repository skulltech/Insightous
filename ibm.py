import json
from watson_developer_cloud import PersonalityInsightsV3



def personality_insights(username, password, data):
    insights = PersonalityInsightsV3(
        version='2016-10-20',
        username='YOUR SERVICE USERNAME',
        password='YOUR SERVICE PASSWORD')

    profile = personality_insights.profile(data, content_type='application/json',
                                           raw_scores=True, consumption_preferences=True)
    print(json.dumps(profile, indent=2))
