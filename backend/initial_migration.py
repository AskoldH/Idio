def insertData(apps, schema_editor):
            # edu videos
            EduVideoModel = apps.get_model('idio_main', 'EduVideo')

            edu_video_1 = EduVideoModel(
                name="Tedův úvodní proslov", video_file="videos/HIMYM_1.mp4",
                main_thought="Ted si chce pokecat", source_type="TV-series", source_info="How I met your mother S1E1")

            edu_video_2 = EduVideoModel(
                name="Marshall trénuje \"vezmeš si mě\"", video_file="videos/HIMYM_2.mp4",
                main_thought="Vezmeš si mě a nespěte v naší kuchyni prosím", source_type="TV-series", source_info="How I met your mother S1E1")

            # save videos
            edu_video_1.save()
            edu_video_2.save()
            
            # subtitles
            # 1st video
            SubtitlesInfoModel = apps.get_model('idio_main', 'SubtitlesInfo')
            subttiles_info_1 = SubtitlesInfoModel(start_time="0",
                                                original="Kids, I'm gonna tell you an incredible story.",
                                                translation="Děti, povím vám úžasný příběh.",
                                                edu_video=edu_video_1)

            subttiles_info_2 = SubtitlesInfoModel(start_time="4.25",
                                                original="The story of how I met your mother.",
                                                translation="Příbeh o tom, jak jsem poznal vaši matku.",
                                                edu_video=edu_video_1)

            
            subttiles_info_3 = SubtitlesInfoModel(start_time="6.5",
                                                original="Are we being punished for something?",
                                                translation="Ty nás za něco trestáš?",
                                                edu_video=edu_video_1)

            # 2nd video
            subttiles_info_4 = SubtitlesInfoModel(start_time="0",
                                                original="Will you marry me?",
                                                translation="Vezmeš si mě?",
                                                edu_video=edu_video_2)
            
            subttiles_info_5 = SubtitlesInfoModel(start_time="1",
                                                original="Yes! Perfect, and then you're engaged,",
                                                translation="Ano! Perfektní, pak jsi už zasnoubený,",
                                                edu_video=edu_video_2)
            
            subttiles_info_6 = SubtitlesInfoModel(start_time="5",
                                                original="you pop the champane, you drink a toast,",
                                                translation="vystřelíte šampaňské, připijete si,",
                                                edu_video=edu_video_2)

            subttiles_info_7 = SubtitlesInfoModel(start_time="6.5",
                                                original="you have sex on the kitchen floor.",
                                                translation="vyspíte se v kuchyni na zemi.",
                                                edu_video=edu_video_2)    

            subttiles_info_8 = SubtitlesInfoModel(start_time="8",
                                                original="Don't have sex on our kitchen floor.",
                                                translation="Nedělejte to v kuchyni na zemi.",
                                                edu_video=edu_video_2)    

            # save subtitles
            subttiles_info_1.save()
            subttiles_info_2.save()
            subttiles_info_3.save()
            subttiles_info_4.save()
            subttiles_info_5.save()
            subttiles_info_6.save()
            subttiles_info_7.save()
            subttiles_info_8.save()


migrations.RunPython(insertData)