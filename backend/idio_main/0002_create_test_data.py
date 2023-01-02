from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = False

    dependencies = [
        ('idio_main', '0001_initial'),
    ]

    def insertData(apps, schema_editor):
        print(" Running creating test data...")
        # edu videos sources
        VideoSourcesType = apps.get_model('idio_main', 'VideoSourcesType')
        VideoSourceName = apps.get_model('idio_main', 'VideoSourceName')

        edu_source_type_1 = VideoSourcesType(
            video_source_type="TV-Series", label="Seriál")
        edu_source_type_2 = VideoSourcesType(
            video_source_type="Film", label="Film")

        edu_source_name_1 = VideoSourceName(source_name_en="How I met your mother",
                                            source_name_cs="Jak jsem poznal vaši matku", source_season_episode="S1E1")

        edu_source_name_2 = VideoSourceName(source_name_en="How I met your mother",
                                            source_name_cs="Jak jsem poznal vaši matku", source_season_episode="S1E2")

        edu_source_name_3 = VideoSourceName(source_name_en="How I met your mother",
                                            source_name_cs="Jak jsem poznal vaši matku", source_season_episode="S1E20")
        edu_source_type_1.save()
        edu_source_type_2.save()
        edu_source_name_1.save()
        edu_source_name_2.save()
        edu_source_name_3.save()

        # edu videos
        EduVideoModel = apps.get_model('idio_main', 'EduVideo')

        video_file_1 = "videos/HIMYM_1.mp4"
        video_file_2 = "videos/HIMYM_2.mp4"
        video_file_3 = "videos/HIMYM_3.mp4"
        video_file_4 = "videos/HIMYM_4.mp4"

        edu_video_1 = EduVideoModel(
            name="Tedův úvodní proslov", video_file=video_file_1,
            main_thought="Ted si chce pokecat", source_type=edu_source_type_1,
            source_info=edu_source_name_1)

        edu_video_2 = EduVideoModel(
            name="Marshall trénuje \"vezmeš si mě\"", video_file=video_file_2,
            main_thought="Vezmeš si mě a nespěte v naší kuchyni prosím", source_type=edu_source_type_1,
            source_info=edu_source_name_1)

        edu_video_3 = EduVideoModel(
            name="Ted mluví o prvním setkání s Robin", video_file=video_file_3,
            main_thought="Ted se chce oženit a náhodou potkává Robin", source_type=edu_source_type_1,
            source_info=edu_source_name_2)
        
        edu_video_4 = EduVideoModel(
            name="Van Smoot je k mání", video_file=video_file_3,
            main_thought="Ve Van Smoot house se uvolnil termín", source_type=edu_source_type_1,
            source_info=edu_source_name_3)


        # save videos
        edu_video_1.save()
        edu_video_2.save()
        edu_video_3.save()
        edu_video_4.save()

        # subtitles
        # 1st video
        SubtitlesInfoModel = apps.get_model('idio_main', 'SubtitlesInfo')
        subtitles_info_1_1 = SubtitlesInfoModel(start_time="0.25",
                                              original="Kids, I'm gonna tell you an incredible story.",
                                              translation="Děti, povím vám úžasný příběh.",
                                              edu_video=edu_video_1)

        subtitles_info_1_2 = SubtitlesInfoModel(start_time="4.25",
                                              original="The story of how I met your mother.",
                                              translation="Příbeh o tom, jak jsem poznal vaši matku.",
                                              edu_video=edu_video_1)

        subtitles_info_1_3 = SubtitlesInfoModel(start_time="6.5",
                                              original="Are we being punished for something?",
                                              translation="Ty nás za něco trestáš?",
                                              edu_video=edu_video_1)

        # 2nd video
        subtitles_info_2_1 = SubtitlesInfoModel(start_time="0.25",
                                              original="Will you marry me?",
                                              translation="Vezmeš si mě?",
                                              edu_video=edu_video_2)

        subtitles_info_2_2 = SubtitlesInfoModel(start_time="1",
                                              original="Yes! Perfect, and then you're engaged,",
                                              translation="Ano! Perfektní, pak jsi už zasnoubený,",
                                              edu_video=edu_video_2)

        subtitles_info_2_3 = SubtitlesInfoModel(start_time="5",
                                              original="you pop the champane, you drink a toast,",
                                              translation="vystřelíte šampaňské, připijete si,",
                                              edu_video=edu_video_2)

        subtitles_info_2_4 = SubtitlesInfoModel(start_time="6.5",
                                              original="you have sex on the kitchen floor.",
                                              translation="vyspíte se v kuchyni na zemi.",
                                              edu_video=edu_video_2)

        subtitles_info_2_5 = SubtitlesInfoModel(start_time="8",
                                              original="Don't have sex on our kitchen floor.",
                                              translation="Nedělejte to v kuchyni na zemi.",
                                              edu_video=edu_video_2)

        # 3rd video
        subtitles_info_3_1 = SubtitlesInfoModel(start_time="0.25",
                                              original="My two best friends got engaged",
                                              translation="Dva moji nejlepší kámoši se zasnoubili",
                                              edu_video=edu_video_3)

        subtitles_info_3_2 = SubtitlesInfoModel(start_time="1.25",
                                              original="and it got me tkinking, ",
                                              translation="a díky tomu jsem začal přemýšlet",
                                              edu_video=edu_video_3)

        subtitles_info_3_3 = SubtitlesInfoModel(start_time="3.0",
                                              original="maybe I should get married.",
                                              translation="že bych se měl možná už oženit.",
                                              edu_video=edu_video_3)

        subtitles_info_3_4 = SubtitlesInfoModel(start_time="4.75",
                                              original="And then I saw Robin, ",
                                              translation="A pak jsem uviděl Robin, ",
                                              edu_video=edu_video_3)

        subtitles_info_3_5 = SubtitlesInfoModel(start_time="6.75",
                                              original="she was incredible.",
                                              translation="byla neuvěřitelná.",
                                              edu_video=edu_video_3)                                      

        subtitles_info_3_6 = SubtitlesInfoModel(start_time="8.5",
                                              original="I just knew I had to meet her.",
                                              translation="Věděl jsem, že ji musím poznat.",
                                              edu_video=edu_video_3) 

        # 4th video
        subtitles_info_4_1 = SubtitlesInfoModel(start_time="0.25",
                                              original="Van Smoot is available.",
                                              translation="Van Smoot je volný.",
                                              edu_video=edu_video_4)

        subtitles_info_4_2 = SubtitlesInfoModel(start_time="1",
                                              original="Oh my god!",
                                              translation="Ó můj bože!",
                                              edu_video=edu_video_4)

        subtitles_info_4_3 = SubtitlesInfoModel(start_time="2",
                                              original="Van Smoot house was a gorgeous mansion",
                                              translation="Van Smoot bylo nádherné panství",
                                              edu_video=edu_video_4)

        subtitles_info_4_4 = SubtitlesInfoModel(start_time="4.75",
                                              original="right on the Hudson River.",
                                              translation="které leželo na řece Hudson.",
                                              edu_video=edu_video_4)

        subtitles_info_4_5 = SubtitlesInfoModel(start_time="6",
                                              original="It had everything Marshall and Lily wanted for their wedding,",
                                              translation="Bylo tam vše, co Marshall a Lili chtěli na svojí svatbě,",
                                              edu_video=edu_video_4)
        
        subtitles_info_4_5 = SubtitlesInfoModel(start_time="8.5",
                                              original="but it was never available and then, suddenly, it was.",
                                              translation="ale nikdo tam neměli volno, ale pak najednou ano.",
                                              edu_video=edu_video_4)


        # save subtitles
        # 1
        subtitles_info_1_1.save()
        subtitles_info_1_2.save()
        subtitles_info_1_3.save()
        
        # 2
        subtitles_info_2_1.save()
        subtitles_info_2_2.save()
        subtitles_info_2_3.save()
        subtitles_info_2_4.save()
        subtitles_info_2_5.save()
        
        # 3
        subtitles_info_3_1.save()
        subtitles_info_3_2.save()
        subtitles_info_3_3.save()
        subtitles_info_3_4.save()
        subtitles_info_3_5.save()
        subtitles_info_3_6.save()

        # 4
        subtitles_info_4_1.save()
        subtitles_info_4_2.save()
        subtitles_info_4_3.save()
        subtitles_info_4_4.save()
        subtitles_info_4_5.save()

    operations = [
        migrations.RunPython(insertData)
    ]
