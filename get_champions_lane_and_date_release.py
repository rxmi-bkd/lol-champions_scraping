import pandas as pd

from bs4 import BeautifulSoup

html = """

<table class="stdt sortable jquery-tablesorter" style="text-align:center; border-collapse:collapse; border:1px solid #191919; width:95%; color:white;" cellspacing="1" cellpadding="1" border="1" align="center" data-index-number="0">

<thead><tr style="white-space: nowrap">
<th bgcolor="#333333" class="headerSort" tabindex="0" role="columnheader button" title="Tri croissant">Champion
</th>
<th bgcolor="#333333" class="headerSort" tabindex="0" role="columnheader button" title="Tri croissant">Classe
</th>
<th class="headerSort" tabindex="0" role="columnheader button" title="Tri croissant">Rôle Principal
</th>
<th bgcolor="#333333" class="headerSort" tabindex="0" role="columnheader button" title="Tri croissant">Date
</th>
<th bgcolor="#333333" class="headerSort" tabindex="0" role="columnheader button" title="Tri croissant"><span style="white-space: nowrap;"><a href="/fr/wiki/Essence_Bleue" title="Essence Bleue"><img alt="PI" src="https://static.wikia.nocookie.net/leagueoflegends/images/c/cf/EB.png/revision/latest/scale-to-width-down/15?cb=20221215225757&amp;path-prefix=fr" decoding="async" loading="lazy" width="15" height="17" data-image-name="EB.png" data-image-key="EB.png" data-relevant="0"></a> </span>
</th>
<th bgcolor="#333333" class="headerSort" tabindex="0" role="columnheader button" title="Tri croissant"><span style="white-space: nowrap;"><a href="/fr/wiki/Riot_Points" title="Riot Points"><img alt="RP" src="https://static.wikia.nocookie.net/leagueoflegends/images/8/8c/RpPoints.png/revision/latest/scale-to-width-down/20?cb=20221015163146&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="RpPoints.png" data-image-key="RpPoints.png" data-relevant="0"></a></span>
</th></tr></thead><tbody>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Aatrox" title="Aatrox"><img alt="AatroxPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/9/9b/AatroxPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712170227&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="AatroxPortrait.png" data-image-key="AatroxPortrait.png" data-relevant="0"></a> <span><a href="/fr/wiki/Aatrox" title="Aatrox">Aatrox</a></span></span>, Épée des Darkins
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">13/06/2013
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Ahri" title="Ahri"><img alt="AhriPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/3/30/AhriPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105212508&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="AhriPortrait.png" data-image-key="AhriPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/3/30/AhriPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105212508&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Ahri" title="Ahri">Ahri</a></span></span>, Renard à neuf queues
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">14/12/2011
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Akali" title="Akali"><img alt="AkaliPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/f/fc/AkaliPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712171451&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="AkaliPortrait.png" data-image-key="AkaliPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/f/fc/AkaliPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712171451&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Akali" title="Akali">Akali</a></span></span>, Assassin rebelle
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Mid
</td>
<td bgcolor="#242424">11/05/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Akshan" title="Akshan"><img alt="AkshanPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e1/AkshanPortrait.png/revision/latest/scale-to-width-down/20?cb=20210725104657&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="AkshanPortrait.png" data-image-key="AkshanPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e1/AkshanPortrait.png/revision/latest/scale-to-width-down/20?cb=20210725104657&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Akshan" title="Akshan">Akshan</a></span></span>, Sentinelle rebelle
</td>
<td bgcolor="#242424">Tireur
</td>
<td>Mid
</td>
<td bgcolor="#242424">23/07/2021
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Alistar" title="Alistar"><img alt="AlistarPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4f/AlistarPortrait.png/revision/latest/scale-to-width-down/20?cb=20150109064000&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="AlistarPortrait.png" data-image-key="AlistarPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4f/AlistarPortrait.png/revision/latest/scale-to-width-down/20?cb=20150109064000&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Alistar" title="Alistar">Alistar</a></span></span>, Minotaure
</td>
<td bgcolor="#242424">Tank
</td>
<td>Support
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Amumu" title="Amumu"><img alt="AmumuPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/b/b1/AmumuPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630013909&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="AmumuPortrait.png" data-image-key="AmumuPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/b/b1/AmumuPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630013909&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Amumu" title="Amumu">Amumu</a></span></span>, Momie mélancolique
</td>
<td bgcolor="#242424">Tank
</td>
<td>Jungle
</td>
<td bgcolor="#242424">26/06/2009
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Anivia" title="Anivia"><img alt="AniviaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/3/35/AniviaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150610151354&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="AniviaPortrait.png" data-image-key="AniviaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/3/35/AniviaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150610151354&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Anivia" title="Anivia">Anivia</a></span></span>, Cryophénix
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">10/07/2009
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Annie" title="Annie"><img alt="AnniePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/dd/AnniePortrait.png/revision/latest/scale-to-width-down/20?cb=20130129063726&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="AnniePortrait.png" data-image-key="AnniePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/dd/AnniePortrait.png/revision/latest/scale-to-width-down/20?cb=20130129063726&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Annie" title="Annie">Annie</a></span></span>, Enfant des ténèbres
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Aphelios" title="Aphelios"><img alt="ApheliosPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d5/ApheliosPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712171554&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ApheliosPortrait.png" data-image-key="ApheliosPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d5/ApheliosPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712171554&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Aphelios" title="Aphelios">Aphelios</a></span></span>, Arme des Lunaris
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">11/12/2019
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Ashe" title="Ashe"><img alt="AshePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c1/AshePortrait.png/revision/latest/scale-to-width-down/20?cb=20140131222657&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="AshePortrait.png" data-image-key="AshePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c1/AshePortrait.png/revision/latest/scale-to-width-down/20?cb=20140131222657&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Ashe" title="Ashe">Ashe</a></span></span>, Archère de givre
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Aurelion_Sol" title="Aurelion Sol"><img alt="AurelionSolPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/3/3f/AurelionSolPortrait.png/revision/latest/scale-to-width-down/20?cb=20160405121342&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="AurelionSolPortrait.png" data-image-key="AurelionSolPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/3/3f/AurelionSolPortrait.png/revision/latest/scale-to-width-down/20?cb=20160405121342&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Aurelion_Sol" title="Aurelion Sol">Aurelion Sol</a></span></span>, Forgeur d'étoiles
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">24/03/2016
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Azir" title="Azir"><img alt="AzirPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e2/AzirPortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223435&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="AzirPortrait.png" data-image-key="AzirPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e2/AzirPortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223435&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Azir" title="Azir">Azir</a></span></span>, Empereur des sables
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">16/09/2014
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Bard" title="Bard"><img alt="BardPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/0a/BardPortrait.png/revision/latest/scale-to-width-down/20?cb=20150224203920&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="BardPortrait.png" data-image-key="BardPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/0a/BardPortrait.png/revision/latest/scale-to-width-down/20?cb=20150224203920&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Bard" title="Bard">Bard</a></span></span>, Gardien errant
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">12/03/2015
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Bel%27Veth" title="Bel'Veth"><img alt="BelVethPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/00/BelVethPortrait.png/revision/latest/scale-to-width-down/20?cb=20220927185747&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="BelVethPortrait.png" data-image-key="BelVethPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/00/BelVethPortrait.png/revision/latest/scale-to-width-down/20?cb=20220927185747&amp;path-prefix=fr" class=" lazyloaded"></a> <span><span class="new" title="Bel'Veth (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvQmVsJTI3VmV0aD9hY3Rpb249ZWRpdCZyZWRsaW5rPTE=">Bel'Veth</span></span></span>, Impératrice du Néant
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">09/06/2022
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Blitzcrank" title="Blitzcrank"><img alt="BlitzcrankPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/2/27/BlitzcrankPortrait.png/revision/latest/scale-to-width-down/20?cb=20141013200939&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="BlitzcrankPortrait.png" data-image-key="BlitzcrankPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/2/27/BlitzcrankPortrait.png/revision/latest/scale-to-width-down/20?cb=20141013200939&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Blitzcrank" title="Blitzcrank">Blitzcrank</a></span></span>, Golem de vapeur
</td>
<td bgcolor="#242424">Tank
</td>
<td>Support
</td>
<td bgcolor="#242424">02/09/2009
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Brand" title="Brand"><img alt="BrandPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e8/BrandPortrait.png/revision/latest/scale-to-width-down/20?cb=20121128074317&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="BrandPortrait.png" data-image-key="BrandPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e8/BrandPortrait.png/revision/latest/scale-to-width-down/20?cb=20121128074317&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Brand" title="Brand">Brand</a></span></span>, Vengeur flamboyant
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">12/04/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Braum" title="Braum"><img alt="BraumPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/db/BraumPortrait.png/revision/latest/scale-to-width-down/20?cb=20140527122948&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="BraumPortrait.png" data-image-key="BraumPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/db/BraumPortrait.png/revision/latest/scale-to-width-down/20?cb=20140527122948&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Braum" title="Braum">Braum</a></span></span>, Cœur de Freljord
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">12/05/2014
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Briar" title="Briar"><img alt="BriarPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f8/BriarPortrait.png/revision/latest/scale-to-width-down/20?cb=20240120235117&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="BriarPortrait.png" data-image-key="BriarPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f8/BriarPortrait.png/revision/latest/scale-to-width-down/20?cb=20240120235117&amp;path-prefix=fr" class=" lazyloaded"></a> <span><span class="new" title="Briar (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvQnJpYXI/YWN0aW9uPWVkaXQmcmVkbGluaz0x">Briar</span></span></span>
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">14/09/2023
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Caitlyn" title="Caitlyn"><img alt="CaitlynPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/5/57/CaitlynPortrait.png/revision/latest/scale-to-width-down/20?cb=20140703174858&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="CaitlynPortrait.png" data-image-key="CaitlynPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/5/57/CaitlynPortrait.png/revision/latest/scale-to-width-down/20?cb=20140703174858&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Caitlyn" title="Caitlyn">Caitlyn</a></span></span>, Shérif de Piltover
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">04/01/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Camille" title="Camille"><img alt="CamillePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/b/b7/CamillePortrait.png/revision/latest/scale-to-width-down/20?cb=20170115123349&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="CamillePortrait.png" data-image-key="CamillePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/b/b7/CamillePortrait.png/revision/latest/scale-to-width-down/20?cb=20170115123349&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Camille" title="Camille">Camille</a></span></span>, Ombre d'acier
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">07/12/2016
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Cassiopeia" title="Cassiopeia"><img alt="CassiopeiaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/b/b1/CassiopeiaPortrait.png/revision/latest/scale-to-width-down/20?cb=20140927221515&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="CassiopeiaPortrait.png" data-image-key="CassiopeiaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/b/b1/CassiopeiaPortrait.png/revision/latest/scale-to-width-down/20?cb=20140927221515&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Cassiopeia" title="Cassiopeia">Cassiopeia</a></span></span>, Étreinte du serpent
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">14/12/2010
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Cho%27Gath" title="Cho'Gath"><img alt="ChoGathPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/b/bf/Cho%27GathPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105212358&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="Cho'GathPortrait.png" data-image-key="Cho%27GathPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/b/bf/Cho%27GathPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105212358&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Cho%27Gath" title="Cho'Gath">Cho'Gath</a></span></span>, Terreur noire
</td>
<td bgcolor="#242424">Tank
</td>
<td>Top
</td>
<td bgcolor="#242424">26/06/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Corki" title="Corki"><img alt="CorkiPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/6/65/CorkiPortrait.png/revision/latest/scale-to-width-down/20?cb=20120804072131&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="CorkiPortrait.png" data-image-key="CorkiPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/6/65/CorkiPortrait.png/revision/latest/scale-to-width-down/20?cb=20120804072131&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Corki" title="Corki">Corki</a></span></span>, Artilleur téméraire
</td>
<td bgcolor="#242424">Tireur
</td>
<td>Mid
</td>
<td bgcolor="#242424">19/09/2009
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Darius" title="Darius"><img alt="DariusPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/6/6e/DariusPortrait.png/revision/latest/scale-to-width-down/20?cb=20160425190134&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="DariusPortrait.png" data-image-key="DariusPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/6/6e/DariusPortrait.png/revision/latest/scale-to-width-down/20?cb=20160425190134&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Darius" title="Darius">Darius</a></span></span>, Main de Noxus
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">23/05/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Diana" title="Diana"><img alt="DianaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f5/DianaPortrait.png/revision/latest/scale-to-width-down/20?cb=20120728030158&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="DianaPortrait.png" data-image-key="DianaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f5/DianaPortrait.png/revision/latest/scale-to-width-down/20?cb=20120728030158&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Diana" title="Diana">Diana</a></span></span>, Mépris de la lune
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">07/08/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Dr._Mundo" title="Dr. Mundo"><img alt="DrMundoPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/0b/Dr._MundoPortrait.png/revision/latest/scale-to-width-down/20?cb=20220927190430&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="Dr. MundoPortrait.png" data-image-key="Dr._MundoPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/0b/Dr._MundoPortrait.png/revision/latest/scale-to-width-down/20?cb=20220927190430&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Dr._Mundo" title="Dr. Mundo">Dr. Mundo</a></span></span>, Dément de Zaun
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">02/09/2009
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Draven" title="Draven"><img alt="DravenPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/3/33/DravenPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630014617&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="DravenPortrait.png" data-image-key="DravenPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/3/33/DravenPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630014617&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Draven" title="Draven">Draven</a></span></span>, Glorieux exécuteur
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">06/06/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Ekko" title="Ekko"><img alt="EkkoPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/1/10/EkkoPortrait.png/revision/latest/scale-to-width-down/20?cb=20150513200331&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="EkkoPortrait.png" data-image-key="EkkoPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/1/10/EkkoPortrait.png/revision/latest/scale-to-width-down/20?cb=20150513200331&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Ekko" title="Ekko">Ekko</a></span></span>, Fractureur du temps
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Jungle
</td>
<td bgcolor="#242424">29/05/2015
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Elise" title="Elise"><img alt="ElisePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/1/1a/ElisePortrait.png/revision/latest/scale-to-width-down/20?cb=20121023032747&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ElisePortrait.png" data-image-key="ElisePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/1/1a/ElisePortrait.png/revision/latest/scale-to-width-down/20?cb=20121023032747&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Elise" title="Elise">Elise</a></span></span>,&nbsp;Reine araignée
</td>
<td bgcolor="#242424">Mage
</td>
<td>Jungle
</td>
<td bgcolor="#242424">26/10/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Evelynn" title="Evelynn"><img alt="EvelynnPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/8/8a/EvelynnPortrait.png/revision/latest/scale-to-width-down/20?cb=20180218154006&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="EvelynnPortrait.png" data-image-key="EvelynnPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/8/8a/EvelynnPortrait.png/revision/latest/scale-to-width-down/20?cb=20180218154006&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Evelynn" title="Evelynn">Evelynn</a></span></span>, Démon sadique
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Jungle
</td>
<td bgcolor="#242424">01/05/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Ezreal" title="Ezreal"><img alt="EzrealPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/02/EzrealPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105212406&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="EzrealPortrait.png" data-image-key="EzrealPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/02/EzrealPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105212406&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Ezreal" title="Ezreal">Ezreal</a></span></span>, Explorateur prodigue
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">16/03/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Fiddlesticks" title="Fiddlesticks"><img alt="FiddlesticksPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f5/FiddlesticksPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712171832&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="FiddlesticksPortrait.png" data-image-key="FiddlesticksPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f5/FiddlesticksPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712171832&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Fiddlesticks" title="Fiddlesticks">Fiddlesticks</a></span></span>, Effroi nocturne
</td>
<td bgcolor="#242424">Mage
</td>
<td>Jungle
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Fiora" title="Fiora"><img alt="FioraPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/77/FioraPortrait.png/revision/latest/scale-to-width-down/20?cb=20150803102344&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="FioraPortrait.png" data-image-key="FioraPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/77/FioraPortrait.png/revision/latest/scale-to-width-down/20?cb=20150803102344&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Fiora" title="Fiora">Fiora</a></span></span>, Sublime bretteuse
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">29/02/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Fizz" title="Fizz"><img alt="FizzPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/79/FizzPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630015028&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="FizzPortrait.png" data-image-key="FizzPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/79/FizzPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630015028&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Fizz" title="Fizz">Fizz</a></span></span>, Filou des mers
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Mid
</td>
<td bgcolor="#242424">15/11/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Galio" title="Galio"><img alt="GalioPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4c/GalioPortrait.png/revision/latest/scale-to-width-down/20?cb=20170421212950&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="GalioPortrait.png" data-image-key="GalioPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4c/GalioPortrait.png/revision/latest/scale-to-width-down/20?cb=20170421212950&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Galio" title="Galio">Galio</a></span></span>, Colosse
</td>
<td bgcolor="#242424">Tank
</td>
<td>Mid
</td>
<td bgcolor="#242424">10/08/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Gangplank" title="Gangplank"><img alt="GangplankPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/de/GangplankPortrait.png/revision/latest/scale-to-width-down/20?cb=20150803101817&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="GangplankPortrait.png" data-image-key="GangplankPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/de/GangplankPortrait.png/revision/latest/scale-to-width-down/20?cb=20150803101817&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Gangplank" title="Gangplank">Gangplank</a></span></span>, Fléau des mers
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">19/08/2009
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Garen" title="Garen"><img alt="GarenPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/3/36/GarenPortrait.png/revision/latest/scale-to-width-down/20?cb=20130917235736&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="GarenPortrait.png" data-image-key="GarenPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/3/36/GarenPortrait.png/revision/latest/scale-to-width-down/20?cb=20130917235736&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Garen" title="Garen">Garen</a></span></span>, Force de Demacia
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">27/04/2010
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Gnar" title="Gnar"><img alt="GnarPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/da/GnarPortrait.png/revision/latest/scale-to-width-down/20?cb=20140813175217&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="GnarPortrait.png" data-image-key="GnarPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/da/GnarPortrait.png/revision/latest/scale-to-width-down/20?cb=20140813175217&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Gnar" title="Gnar">Gnar</a></span></span>, Chaînon manquant
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">14/08/2014
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Gragas" title="Gragas"><img alt="GragasPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/5/59/GragasPortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223443&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="GragasPortrait.png" data-image-key="GragasPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/5/59/GragasPortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223443&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Gragas" title="Gragas">Gragas</a></span></span>, Agitateur
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">02/02/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Graves" title="Graves"><img alt="GravesPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/5/58/GravesPortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223448&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="GravesPortrait.png" data-image-key="GravesPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/5/58/GravesPortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223448&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Graves" title="Graves">Graves</a></span></span>, Hors-la-loi
</td>
<td bgcolor="#242424">Tireur
</td>
<td>Jungle
</td>
<td bgcolor="#242424">19/10/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Gwen" title="Gwen"><img alt="GwenPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/78/GwenPortrait.png/revision/latest/scale-to-width-down/20?cb=20210725115228&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="GwenPortrait.png" data-image-key="GwenPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/78/GwenPortrait.png/revision/latest/scale-to-width-down/20?cb=20210725115228&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><span class="new" title="Gwen (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvR3dlbj9hY3Rpb249ZWRpdCZyZWRsaW5rPTE=">Gwen</span></span></span>, Couturière Sacrée
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">15/04/2021
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Hecarim" title="Hecarim"><img alt="HecarimPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d3/HecarimPortrait.png/revision/latest/scale-to-width-down/20?cb=20240916193144&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="HecarimPortrait.png" data-image-key="HecarimPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d3/HecarimPortrait.png/revision/latest/scale-to-width-down/20?cb=20240916193144&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Hecarim" title="Hecarim">Hecarim</a></span></span>, Ombre de la guerre
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">18/04/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Heimerdinger" title="Heimerdinger"><img alt="HeimerdingerPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c0/HeimerdingerPortrait.png/revision/latest/scale-to-width-down/20?cb=20140308175421&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="HeimerdingerPortrait.png" data-image-key="HeimerdingerPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c0/HeimerdingerPortrait.png/revision/latest/scale-to-width-down/20?cb=20140308175421&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Heimerdinger" title="Heimerdinger">Heimerdinger</a></span></span>, Inventeur réputé
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">10/10/2009
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Hwei" title="Hwei"><img alt="HweiPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e9/HweiPortrait.png/revision/latest/scale-to-width-down/20?cb=20240121011604&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="HweiPortrait.png" data-image-key="HweiPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e9/HweiPortrait.png/revision/latest/scale-to-width-down/20?cb=20240121011604&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><span class="new" title="Hwei (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvSHdlaT9hY3Rpb249ZWRpdCZyZWRsaW5rPTE=">Hwei</span></span></span>, Visionnaire
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">05/12/2023
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Illaoi" title="Illaoi"><img alt="IllaoiPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/7e/IllaoiPortrait.png/revision/latest/scale-to-width-down/20?cb=20151113122844&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="IllaoiPortrait.png" data-image-key="IllaoiPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/7e/IllaoiPortrait.png/revision/latest/scale-to-width-down/20?cb=20151113122844&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Illaoi" title="Illaoi">Illaoi</a></span></span>, Prêtresse du kraken
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">24/11/2015
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Irelia" title="Irelia"><img alt="IreliaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d4/IreliaPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712171901&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="IreliaPortrait.png" data-image-key="IreliaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d4/IreliaPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712171901&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Irelia" title="Irelia">Irelia</a></span></span>, Danseuse des lames
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">16/11/2010
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Ivern" title="Ivern"><img alt="IvernPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/44/IvernPortrait.png/revision/latest/scale-to-width-down/20?cb=20170115125308&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="IvernPortrait.png" data-image-key="IvernPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/44/IvernPortrait.png/revision/latest/scale-to-width-down/20?cb=20170115125308&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Ivern" title="Ivern">Ivern</a></span></span>, Ainé de la forêt
</td>
<td bgcolor="#242424">Support
</td>
<td>Jungle
</td>
<td bgcolor="#242424">05/10/2016
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Janna" title="Janna"><img alt="JannaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/48/JannaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223454&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="JannaPortrait.png" data-image-key="JannaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/48/JannaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223454&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Janna" title="Janna">Janna</a></span></span>, Avatar de l'air
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">02/09/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Jarvan_IV" title="Jarvan IV"><img alt="JarvanIVPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c6/Jarvan_IVPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105212747&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="Jarvan IVPortrait.png" data-image-key="Jarvan_IVPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c6/Jarvan_IVPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105212747&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Jarvan_IV" title="Jarvan IV">Jarvan IV</a></span></span>, Exemple demacien
</td>
<td bgcolor="#242424">Tank
</td>
<td>Jungle
</td>
<td bgcolor="#242424">01/03/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Jax" title="Jax"><img alt="JaxPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/2/26/JaxPortrait.png/revision/latest/scale-to-width-down/20?cb=20240916193320&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="JaxPortrait.png" data-image-key="JaxPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/2/26/JaxPortrait.png/revision/latest/scale-to-width-down/20?cb=20240916193320&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Jax" title="Jax">Jax</a></span></span>, Maître d'armes
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Jayce" title="Jayce"><img alt="JaycePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/73/JaycePortrait.png/revision/latest/scale-to-width-down/20?cb=20120704220452&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="JaycePortrait.png" data-image-key="JaycePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/73/JaycePortrait.png/revision/latest/scale-to-width-down/20?cb=20120704220452&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Jayce" title="Jayce">Jayce</a></span></span>, Protecteur du futur
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">07/07/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Jhin" title="Jhin"><img alt="JhinPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/5/57/JhinPortrait.png/revision/latest/scale-to-width-down/20?cb=20160126071702&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="JhinPortrait.png" data-image-key="JhinPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/5/57/JhinPortrait.png/revision/latest/scale-to-width-down/20?cb=20160126071702&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Jhin" title="Jhin">Jhin</a></span></span>, Virtuose
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">01/02/2016
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Jinx" title="Jinx"><img alt="JinxPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/de/JinxPortrait.png/revision/latest/scale-to-width-down/20?cb=20131008180649&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="JinxPortrait.png" data-image-key="JinxPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/de/JinxPortrait.png/revision/latest/scale-to-width-down/20?cb=20131008180649&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Jinx" title="Jinx">Jinx</a></span></span>, Gâchette folle
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">10/10/2013
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/K%27Sant%C3%A9" title="K'Santé"><img alt="KSantéPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/6/69/KSant%C3%A9Portrait.png/revision/latest/scale-to-width-down/20?cb=20230212062955&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="KSantéPortrait.png" data-image-key="KSant%C3%A9Portrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/6/69/KSant%C3%A9Portrait.png/revision/latest/scale-to-width-down/20?cb=20230212062955&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/K%27Sant%C3%A9" title="K'Santé">K'Santé</a></span></span>, Fierté de Nazumah
</td>
<td bgcolor="#242424">Tank
</td>
<td>Top
</td>
<td bgcolor="#242424">02/11/2022
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Kai%27Sa" title="Kai'Sa"><img alt="KaiSaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/9/97/KaiSaPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712204113&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="KaiSaPortrait.png" data-image-key="KaiSaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/9/97/KaiSaPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712204113&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Kai%27Sa" title="Kai'Sa">Kai'Sa</a></span></span>, Fille du Néant
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">07/03/2018
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Kalista" title="Kalista"><img alt="KalistaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c4/KalistaPortrait.png/revision/latest/scale-to-width-down/20?cb=20141112212413&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="KalistaPortrait.png" data-image-key="KalistaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c4/KalistaPortrait.png/revision/latest/scale-to-width-down/20?cb=20141112212413&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Kalista" title="Kalista">Kalista</a></span></span>, Lance de la vengeance
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">20/11/2014
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Karma" title="Karma"><img alt="KarmaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a1/KarmaPortrait.png/revision/latest/scale-to-width-down/20?cb=20160407205325&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="KarmaPortrait.png" data-image-key="KarmaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a1/KarmaPortrait.png/revision/latest/scale-to-width-down/20?cb=20160407205325&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Karma" title="Karma">Karma</a></span></span>, Sagesse incarnée
</td>
<td bgcolor="#242424">Mage
</td>
<td>Support
</td>
<td bgcolor="#242424">01/02/2011
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Karthus" title="Karthus"><img alt="KarthusPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/0c/KarthusPortrait.png/revision/latest/scale-to-width-down/20?cb=20160725131836&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="KarthusPortrait.png" data-image-key="KarthusPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/0c/KarthusPortrait.png/revision/latest/scale-to-width-down/20?cb=20160725131836&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Karthus" title="Karthus">Karthus</a></span></span>, Liche
</td>
<td bgcolor="#242424">Mage
</td>
<td>Jungle
</td>
<td bgcolor="#242424">12/06/2009
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Kassadin" title="Kassadin"><img alt="KassadinPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c0/KassadinPortrait.png/revision/latest/scale-to-width-down/20?cb=20240916193440&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="KassadinPortrait.png" data-image-key="KassadinPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c0/KassadinPortrait.png/revision/latest/scale-to-width-down/20?cb=20240916193440&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Kassadin" title="Kassadin">Kassadin</a></span></span>, Chasseur du Néant
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Mid
</td>
<td bgcolor="#242424">07/08/2009
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Katarina" title="Katarina"><img alt="KatarinaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/43/KatarinaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150218221456&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="KatarinaPortrait.png" data-image-key="KatarinaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/43/KatarinaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150218221456&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Katarina" title="Katarina">Katarina</a></span></span>, Lame sinistre
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Mid
</td>
<td bgcolor="#242424">19/09/2009
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Kayle" title="Kayle"><img alt="KaylePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/1/15/KaylePortrait.png/revision/latest/scale-to-width-down/20?cb=20200712172254&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="KaylePortrait.png" data-image-key="KaylePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/1/15/KaylePortrait.png/revision/latest/scale-to-width-down/20?cb=20200712172254&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Kayle" title="Kayle">Kayle</a></span></span>, Vertueuse
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Kayn" title="Kayn"><img alt="KaynPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d9/KaynPortrait.png/revision/latest/scale-to-width-down/20?cb=20170722210608&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="KaynPortrait.png" data-image-key="KaynPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d9/KaynPortrait.png/revision/latest/scale-to-width-down/20?cb=20170722210608&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Kayn" title="Kayn">Kayn</a></span></span>, Faucheur de l'ombre
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">12/07/2017
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Kennen" title="Kennen"><img alt="KennenPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/08/KennenPortrait.png/revision/latest/scale-to-width-down/20?cb=20170115125652&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="KennenPortrait.png" data-image-key="KennenPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/08/KennenPortrait.png/revision/latest/scale-to-width-down/20?cb=20170115125652&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Kennen" title="Kennen">Kennen</a></span></span>, Cœur de la tempête
</td>
<td bgcolor="#242424">Mage
</td>
<td>Top
</td>
<td bgcolor="#242424">08/04/2010
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Kha%27Zix" title="Kha'Zix"><img alt="KhaZixPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/1/19/Kha%27ZixPortrait.png/revision/latest/scale-to-width-down/20?cb=20120921041105&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="Kha'ZixPortrait.png" data-image-key="Kha%27ZixPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/1/19/Kha%27ZixPortrait.png/revision/latest/scale-to-width-down/20?cb=20120921041105&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Kha%27Zix" title="Kha'Zix">Kha'Zix</a></span></span>, Faucheur du Néant
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Jungle
</td>
<td bgcolor="#242424">27/09/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Kindred" title="Kindred"><img alt="KindredPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/7d/KindredPortrait.png/revision/latest/scale-to-width-down/20?cb=20151006142449&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="KindredPortrait.png" data-image-key="KindredPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/7d/KindredPortrait.png/revision/latest/scale-to-width-down/20?cb=20151006142449&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Kindred" title="Kindred">Kindred</a></span></span>, Chasseurs éternels
</td>
<td bgcolor="#242424">Tireur
</td>
<td>Jungle
</td>
<td bgcolor="#242424">14/10/2015
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Kled" title="Kled"><img alt="KledPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/42/KledPortrait.png/revision/latest/scale-to-width-down/20?cb=20170115125822&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="KledPortrait.png" data-image-key="KledPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/42/KledPortrait.png/revision/latest/scale-to-width-down/20?cb=20170115125822&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Kled" title="Kled">Kled</a></span></span>, Cavalier colérique
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">10/08/2016
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Kog%27Maw" title="Kog'Maw"><img alt="KogMawPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/9/97/Kog%27MawPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105212805&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="Kog'MawPortrait.png" data-image-key="Kog%27MawPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/9/97/Kog%27MawPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105212805&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Kog%27Maw" title="Kog'Maw">Kog'Maw</a></span></span>, Gueule des abysses
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">24/06/2010
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/LeBlanc" title="LeBlanc"><img alt="LeBlancPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/b/b6/LeBlancPortrait.png/revision/latest/scale-to-width-down/20?cb=20121128074551&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="LeBlancPortrait.png" data-image-key="LeBlancPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/b/b6/LeBlancPortrait.png/revision/latest/scale-to-width-down/20?cb=20121128074551&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/LeBlanc" title="LeBlanc">LeBlanc</a></span></span>, Manipulatrice
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Mid
</td>
<td bgcolor="#242424">02/11/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Lee_Sin" title="Lee Sin"><img alt="LeeSinPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/1/11/Lee_SinPortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223503&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="Lee SinPortrait.png" data-image-key="Lee_SinPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/1/11/Lee_SinPortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223503&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Lee_Sin" title="Lee Sin">Lee Sin</a></span></span>, Moine aveugle
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">02/04/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Leona" title="Leona"><img alt="LeonaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f0/LeonaPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630030937&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="LeonaPortrait.png" data-image-key="LeonaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f0/LeonaPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630030937&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Leona" title="Leona">Leona</a></span></span>, Aube radieuse
</td>
<td bgcolor="#242424">Tank
</td>
<td>Support
</td>
<td bgcolor="#242424">13/07/2011
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Lillia" title="Lillia"><img alt="LilliaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/43/LilliaPortrait.png/revision/latest/scale-to-width-down/20?cb=20210725115320&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="LilliaPortrait.png" data-image-key="LilliaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/43/LilliaPortrait.png/revision/latest/scale-to-width-down/20?cb=20210725115320&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Lillia" title="Lillia">Lillia</a></span></span>, Fleur timide
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">22/07/2020
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Lissandra" title="Lissandra"><img alt="LissandraPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c6/LissandraPortrait.png/revision/latest/scale-to-width-down/20?cb=20130404051613&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="LissandraPortrait.png" data-image-key="LissandraPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c6/LissandraPortrait.png/revision/latest/scale-to-width-down/20?cb=20130404051613&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Lissandra" title="Lissandra">Lissandra</a></span></span>, Sorcière de glace
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">30/04/2013
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Lucian" title="Lucian"><img alt="LucianPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/2/2e/LucianPortrait.png/revision/latest/scale-to-width-down/20?cb=20130713055752&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="LucianPortrait.png" data-image-key="LucianPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/2/2e/LucianPortrait.png/revision/latest/scale-to-width-down/20?cb=20130713055752&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Lucian" title="Lucian">Lucian</a></span></span>, Purificateur
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">22/08/2013
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Lulu" title="Lulu"><img alt="LuluPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/1/13/LuluPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630030956&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="LuluPortrait.png" data-image-key="LuluPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/1/13/LuluPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630030956&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Lulu" title="Lulu">Lulu</a></span></span>, Sorcière féerique
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">20/03/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Lux" title="Lux"><img alt="LuxPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/5/52/LuxPortrait.png/revision/latest/scale-to-width-down/20?cb=20121005030826&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="LuxPortrait.png" data-image-key="LuxPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/5/52/LuxPortrait.png/revision/latest/scale-to-width-down/20?cb=20121005030826&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Lux" title="Lux">Lux</a></span></span>, Dame de lumière
</td>
<td bgcolor="#242424">Mage
</td>
<td>Support
</td>
<td bgcolor="#242424">19/10/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Ma%C3%AEtre_Yi" title="Maître Yi"><img alt="Maître YiPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/1/1b/Ma%C3%AEtreYiPortrait.png/revision/latest/scale-to-width-down/20?cb=20130327224933&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="MaîtreYiPortrait.png" data-image-key="Ma%C3%AEtreYiPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/1/1b/Ma%C3%AEtreYiPortrait.png/revision/latest/scale-to-width-down/20?cb=20130327224933&amp;path-prefix=fr" class=" lazyloaded"></a> <span><a href="/fr/wiki/Ma%C3%AEtre_Yi" title="Maître Yi">Maître&nbsp;Yi</a></span></span>, Fine lame Wuju
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Jungle
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Malphite" title="Malphite"><img alt="MalphitePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/5/52/MalphitePortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213000&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="MalphitePortrait.png" data-image-key="MalphitePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/5/52/MalphitePortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213000&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Malphite" title="Malphite">Malphite</a></span></span>, Éclat du monolithe
</td>
<td bgcolor="#242424">Tank
</td>
<td>Top
</td>
<td bgcolor="#242424">02/09/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Malzahar" title="Malzahar"><img alt="MalzaharPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/e/ec/MalzaharPortrait.png/revision/latest/scale-to-width-down/20?cb=20160611163128&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="MalzaharPortrait.png" data-image-key="MalzaharPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/e/ec/MalzaharPortrait.png/revision/latest/scale-to-width-down/20?cb=20160611163128&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Malzahar" title="Malzahar">Malzahar</a></span></span>, Prophète du Néant
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">01/06/2010
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Maokai" title="Maokai"><img alt="MaokaiPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/9/94/MaokaiPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213008&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="MaokaiPortrait.png" data-image-key="MaokaiPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/9/94/MaokaiPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213008&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Maokai" title="Maokai">Maokai</a></span></span>, Tréant torturé
</td>
<td bgcolor="#242424">Tank
</td>
<td>Support
</td>
<td bgcolor="#242424">16/02/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Milio" title="Milio"><img alt="MilioPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/3/3a/MilioPortrait.png/revision/latest/scale-to-width-down/20?cb=20240120235232&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="MilioPortrait.png" data-image-key="MilioPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/3/3a/MilioPortrait.png/revision/latest/scale-to-width-down/20?cb=20240120235232&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Milio" title="Milio">Milio</a></span></span> Douce Flamme
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">22/03/2023
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Miss_Fortune" title="Miss Fortune"><img alt="MissFortunePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c9/MissFortunePortrait.png/revision/latest/scale-to-width-down/20?cb=20160725132028&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="MissFortunePortrait.png" data-image-key="MissFortunePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c9/MissFortunePortrait.png/revision/latest/scale-to-width-down/20?cb=20160725132028&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Miss_Fortune" title="Miss Fortune">Miss Fortune</a></span></span> Chasseuse de primes
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">08/09/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Mordekaiser" title="Mordekaiser"><img alt="MordekaiserPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/71/MordekaiserPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712172413&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="MordekaiserPortrait.png" data-image-key="MordekaiserPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/71/MordekaiserPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712172413&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Mordekaiser" title="Mordekaiser">Mordekaiser</a></span></span>, Revenant de fer
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">24/02/2010
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Morgana" title="Morgana"><img alt="MorganaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/06/MorganaPortrait.png/revision/latest/scale-to-width-down/20?cb=20220928161625&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="MorganaPortrait.png" data-image-key="MorganaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/06/MorganaPortrait.png/revision/latest/scale-to-width-down/20?cb=20220928161625&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Morgana" title="Morgana">Morgana</a></span></span>, Déchue
</td>
<td bgcolor="#242424">Mage
</td>
<td>Support
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Naafiri" title="Naafiri"><img alt="NaafiriPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/9/9b/NaafiriPortrait.png/revision/latest/scale-to-width-down/20?cb=20240120235423&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="NaafiriPortrait.png" data-image-key="NaafiriPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/9/9b/NaafiriPortrait.png/revision/latest/scale-to-width-down/20?cb=20240120235423&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><span class="new" title="Naafiri (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvTmFhZmlyaT9hY3Rpb249ZWRpdCZyZWRsaW5rPTE=">Naafiri</span></span></span>, La meute de Fer
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Mid
</td>
<td bgcolor="#242424">19/07/2023
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Nami" title="Nami"><img alt="NamiPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/2/2d/NamiPortrait.png/revision/latest/scale-to-width-down/20?cb=20121130222503&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="NamiPortrait.png" data-image-key="NamiPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/2/2d/NamiPortrait.png/revision/latest/scale-to-width-down/20?cb=20121130222503&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Nami" title="Nami">Nami</a></span></span>, Aquamancienne
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">07/12/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Nasus" title="Nasus"><img alt="NasusPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/45/NasusPortrait.png/revision/latest/scale-to-width-down/20?cb=20131113195805&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="NasusPortrait.png" data-image-key="NasusPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/45/NasusPortrait.png/revision/latest/scale-to-width-down/20?cb=20131113195805&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Nasus" title="Nasus">Nasus</a></span></span>, Gardien des sables
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">01/10/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Nautilus" title="Nautilus"><img alt="NautilusPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/8/83/NautilusPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630031356&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="NautilusPortrait.png" data-image-key="NautilusPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/8/83/NautilusPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630031356&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Nautilus" title="Nautilus">Nautilus</a></span></span>, Titan des profondeurs
</td>
<td bgcolor="#242424">Tank
</td>
<td>Support
</td>
<td bgcolor="#242424">14/02/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Neeko" title="Neeko"><img alt="NeekoPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/c/cf/NeekoPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712183009&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="NeekoPortrait.png" data-image-key="NeekoPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/c/cf/NeekoPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712183009&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Neeko" title="Neeko">Neeko</a></span></span>,&nbsp;Caméléon curieux
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">05/12/2018
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Nidalee" title="Nidalee"><img alt="NidaleePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/a/aa/NidaleePortrait.png/revision/latest/scale-to-width-down/20?cb=20121215030439&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="NidaleePortrait.png" data-image-key="NidaleePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/a/aa/NidaleePortrait.png/revision/latest/scale-to-width-down/20?cb=20121215030439&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Nidalee" title="Nidalee">Nidalee</a></span></span>,&nbsp;Chasseresse bestiale
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Jungle
</td>
<td bgcolor="#242424">17/12/2009
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Nilah" title="Nilah"><img alt="NilahPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/dc/NilahPortrait.png/revision/latest/scale-to-width-down/20?cb=20220927185933&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="NilahPortrait.png" data-image-key="NilahPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/dc/NilahPortrait.png/revision/latest/scale-to-width-down/20?cb=20220927185933&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Nilah" title="Nilah">Nilah</a></span></span>, Joie incarnée
</td>
<td bgcolor="#242424">Combattant
</td>
<td>ADC
</td>
<td bgcolor="#242424">13/07/2022
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Nocturne" title="Nocturne"><img alt="NocturnePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/8/84/NocturnePortrait.png/revision/latest/scale-to-width-down/20?cb=20131018031726&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="NocturnePortrait.png" data-image-key="NocturnePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/8/84/NocturnePortrait.png/revision/latest/scale-to-width-down/20?cb=20131018031726&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Nocturne" title="Nocturne">Nocturne</a></span></span>, Éternel cauchemar
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Jungle
</td>
<td bgcolor="#242424">15/03/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Nunu_et_Willump" title="Nunu et Willump"><img alt="NunuetWillumpPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f5/NunuetWillumpPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712172506&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="NunuetWillumpPortrait.png" data-image-key="NunuetWillumpPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f5/NunuetWillumpPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712172506&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Nunu_et_Willump" title="Nunu et Willump">Nunu et Willump</a></span></span>, Le Garçon et son yéti
</td>
<td bgcolor="#242424">Tank
</td>
<td>Jungle
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Olaf" title="Olaf"><img alt="OlafPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/a/ae/OlafPortrait.png/revision/latest/scale-to-width-down/20?cb=20130911223154&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="OlafPortrait.png" data-image-key="OlafPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/a/ae/OlafPortrait.png/revision/latest/scale-to-width-down/20?cb=20130911223154&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Olaf" title="Olaf">Olaf</a></span></span>, Berzerker
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">09/06/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Orianna" title="Orianna"><img alt="OriannaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/b/bd/OriannaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213329&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="OriannaPortrait.png" data-image-key="OriannaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/b/bd/OriannaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213329&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Orianna" title="Orianna">Orianna</a></span></span>, Demoiselle mécanique
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">01/06/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Ornn" title="Ornn"><img alt="OrnnPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/8/82/OrnnPortrait.png/revision/latest/scale-to-width-down/20?cb=20180211131139&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="OrnnPortrait.png" data-image-key="OrnnPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/8/82/OrnnPortrait.png/revision/latest/scale-to-width-down/20?cb=20180211131139&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Ornn" title="Ornn">Ornn</a></span></span>, Dieu de la forge volcanique
</td>
<td bgcolor="#242424">Tank
</td>
<td>Top
</td>
<td bgcolor="#242424">23/08/2017
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Pantheon" title="Pantheon"><img alt="PantheonPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e1/PantheonPortrait.png/revision/latest/scale-to-width-down/20?cb=20190825160944&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="PantheonPortrait.png" data-image-key="PantheonPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e1/PantheonPortrait.png/revision/latest/scale-to-width-down/20?cb=20190825160944&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Pantheon" title="Pantheon">Pantheon</a></span></span>, Lance éternelle
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">02/02/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Poppy" title="Poppy"><img alt="PoppyPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/7c/PoppyPortrait.png/revision/latest/scale-to-width-down/20?cb=20151125124912&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="PoppyPortrait.png" data-image-key="PoppyPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/7c/PoppyPortrait.png/revision/latest/scale-to-width-down/20?cb=20151125124912&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Poppy" title="Poppy">Poppy</a></span></span>, Gardienne du marteau
</td>
<td bgcolor="#242424">Tank
</td>
<td>Top
</td>
<td bgcolor="#242424">13/01/2010
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Pyke" title="Pyke"><img alt="PykePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a9/PykePortrait.png/revision/latest/scale-to-width-down/20?cb=20200712182740&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="PykePortrait.png" data-image-key="PykePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a9/PykePortrait.png/revision/latest/scale-to-width-down/20?cb=20200712182740&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Pyke" title="Pyke">Pyke</a></span></span>, Éventreur des abysses
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">31/05/2018
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Qiyana" title="Qiyana"><img alt="QiyanaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/2/29/QiyanaPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712174521&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="QiyanaPortrait.png" data-image-key="QiyanaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/2/29/QiyanaPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712174521&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><span class="new" title="Qiyana (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvUWl5YW5hP2FjdGlvbj1lZGl0JnJlZGxpbms9MQ==">Qiyana</span></span></span>, Impératrice des éléments
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Mid
</td>
<td bgcolor="#242424">28/06/2018
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Quinn" title="Quinn"><img alt="QuinnPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/f/ff/QuinnPortrait.png/revision/latest/scale-to-width-down/20?cb=20130329043850&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="QuinnPortrait.png" data-image-key="QuinnPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/f/ff/QuinnPortrait.png/revision/latest/scale-to-width-down/20?cb=20130329043850&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Quinn" title="Quinn">Quinn</a></span></span>, Ailes de Demacia
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">01/03/2013
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Rakan" title="Rakan"><img alt="RakanPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/46/RakanPortrait.png/revision/latest/scale-to-width-down/20?cb=20170405212246&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="RakanPortrait.png" data-image-key="RakanPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/46/RakanPortrait.png/revision/latest/scale-to-width-down/20?cb=20170405212246&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Rakan" title="Rakan">Rakan</a></span></span>, Charmeur
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">19/04/2017
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Rammus" title="Rammus"><img alt="RammusPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4e/RammusPortrait.png/revision/latest/scale-to-width-down/20?cb=20160425191020&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="RammusPortrait.png" data-image-key="RammusPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4e/RammusPortrait.png/revision/latest/scale-to-width-down/20?cb=20160425191020&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Rammus" title="Rammus">Rammus</a></span></span>, Tatou blindé
</td>
<td bgcolor="#242424">Tank
</td>
<td>Jungle
</td>
<td bgcolor="#242424">10/07/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Rek%27Sai" title="Rek'Sai"><img alt="RekSaiPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/7c/RekSaiPortrait.png/revision/latest/scale-to-width-down/20?cb=20141126002647&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="RekSaiPortrait.png" data-image-key="RekSaiPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/7c/RekSaiPortrait.png/revision/latest/scale-to-width-down/20?cb=20141126002647&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Rek%27Sai" title="Rek'Sai">Rek'Sai</a></span></span>, Traqueuse du Néant
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">11/12/2014
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Rell" title="Rell"><img alt="RellPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/1/1b/RellPortrait.png/revision/latest/scale-to-width-down/20?cb=20210725114459&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="RellPortrait.png" data-image-key="RellPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/1/1b/RellPortrait.png/revision/latest/scale-to-width-down/20?cb=20210725114459&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><span class="new" title="Rell (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvUmVsbD9hY3Rpb249ZWRpdCZyZWRsaW5rPTE=">Rell</span></span></span>, Vierge de fer
</td>
<td bgcolor="#242424">Tank
</td>
<td>Support
</td>
<td bgcolor="#242424">11/12/2020
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Renata_Glasc" title="Renata Glasc"><img alt="RenataGlascPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/8/85/RenataGlascPortrait.png/revision/latest/scale-to-width-down/20?cb=20220927190036&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="RenataGlascPortrait.png" data-image-key="RenataGlascPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/8/85/RenataGlascPortrait.png/revision/latest/scale-to-width-down/20?cb=20220927190036&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><span class="new" title="Renata Glasc (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvUmVuYXRhX0dsYXNjP2FjdGlvbj1lZGl0JnJlZGxpbms9MQ==">Renata Glasc</span></span></span>, Baronne de la chimie
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">17/02/2022
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Renekton" title="Renekton"><img alt="RenektonPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/7d/RenektonPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213328&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="RenektonPortrait.png" data-image-key="RenektonPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/7d/RenektonPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213328&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Renekton" title="Renekton">Renekton</a></span></span>, Dévoreur des sables
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">18/01/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Rengar" title="Rengar"><img alt="RengarPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/1/1f/RengarPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213337&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="RengarPortrait.png" data-image-key="RengarPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/1/1f/RengarPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213337&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Rengar" title="Rengar">Rengar</a></span></span>, Fier traqueur
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Jungle
</td>
<td bgcolor="#242424">21/08/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Riven" title="Riven"><img alt="RivenPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/0e/RivenPortrait.png/revision/latest/scale-to-width-down/20?cb=20130707182720&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="RivenPortrait.png" data-image-key="RivenPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/0e/RivenPortrait.png/revision/latest/scale-to-width-down/20?cb=20130707182720&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Riven" title="Riven">Riven</a></span></span>, Exilée brisée
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">14/09/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Rumble" title="Rumble"><img alt="RumblePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/02/RumblePortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223510&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="RumblePortrait.png" data-image-key="RumblePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/02/RumblePortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223510&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Rumble" title="Rumble">Rumble</a></span></span>, Menace mécanisée
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">26/04/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Ryze" title="Ryze"><img alt="RyzePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a5/RyzePortrait.png/revision/latest/scale-to-width-down/20?cb=20170102151232&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="RyzePortrait.png" data-image-key="RyzePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a5/RyzePortrait.png/revision/latest/scale-to-width-down/20?cb=20170102151232&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Ryze" title="Ryze">Ryze</a></span></span>, Mage runique
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Samira" title="Samira"><img alt="SamiraPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e9/SamiraPortrait.png/revision/latest/scale-to-width-down/20?cb=20210725115030&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SamiraPortrait.png" data-image-key="SamiraPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e9/SamiraPortrait.png/revision/latest/scale-to-width-down/20?cb=20210725115030&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><span class="new" title="Samira (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvU2FtaXJhP2FjdGlvbj1lZGl0JnJlZGxpbms9MQ==">Samira</span></span></span>, Rose du désert
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">21/09/2021
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Sejuani" title="Sejuani"><img alt="SejuaniPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/2/27/SejuaniPortrait.png/revision/latest/scale-to-width-down/20?cb=20130404053310&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SejuaniPortrait.png" data-image-key="SejuaniPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/2/27/SejuaniPortrait.png/revision/latest/scale-to-width-down/20?cb=20130404053310&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Sejuani" title="Sejuani">Sejuani</a></span></span>, Fureur du nord
</td>
<td bgcolor="#242424">Tank
</td>
<td>Jungle
</td>
<td bgcolor="#242424">17/01/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Senna" title="Senna"><img alt="SennaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/8/85/SennaPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712182422&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SennaPortrait.png" data-image-key="SennaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/8/85/SennaPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712182422&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Senna" title="Senna">Senna</a></span></span>, Rédemptrice
</td>
<td bgcolor="#242424">Tireur
</td>
<td>Support
</td>
<td bgcolor="#242424">10/11/2019
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/S%C3%A9raphine" title="Séraphine"><img alt="SéraphinePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/e/ec/S%C3%A9raphinePortrait.png/revision/latest/scale-to-width-down/20?cb=20220927190116&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SéraphinePortrait.png" data-image-key="S%C3%A9raphinePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/e/ec/S%C3%A9raphinePortrait.png/revision/latest/scale-to-width-down/20?cb=20220927190116&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><span class="new" title="Séraphine (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvUyVDMyVBOXJhcGhpbmU/YWN0aW9uPWVkaXQmcmVkbGluaz0x">Séraphine</span></span></span>, Chanteuse rêveuse
</td>
<td bgcolor="#242424">Mage
</td>
<td>Support
</td>
<td bgcolor="#242424">29/10/2020
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Sett" title="Sett"><img alt="SettPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/05/SettPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712174021&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SettPortrait.png" data-image-key="SettPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/05/SettPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712174021&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Sett" title="Sett">Sett</a></span></span>, Patron
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">14/01/2020
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Shaco" title="Shaco"><img alt="ShacoPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d1/ShacoPortrait.png/revision/latest/scale-to-width-down/20?cb=20141011121531&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ShacoPortrait.png" data-image-key="ShacoPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d1/ShacoPortrait.png/revision/latest/scale-to-width-down/20?cb=20141011121531&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Shaco" title="Shaco">Shaco</a></span></span>, Bouffon des ténèbres
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Jungle
</td>
<td bgcolor="#242424">10/10/2009
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Shen" title="Shen"><img alt="ShenPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f7/ShenPortrait.png/revision/latest/scale-to-width-down/20?cb=20141013201442&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ShenPortrait.png" data-image-key="ShenPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f7/ShenPortrait.png/revision/latest/scale-to-width-down/20?cb=20141013201442&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Shen" title="Shen">Shen</a></span></span>, Œil du crépuscule
</td>
<td bgcolor="#242424">Tank
</td>
<td>Top
</td>
<td bgcolor="#242424">24/03/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Shyvana" title="Shyvana"><img alt="ShyvanaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/08/ShyvanaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213353&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ShyvanaPortrait.png" data-image-key="ShyvanaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/08/ShyvanaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213353&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Shyvana" title="Shyvana">Shyvana</a></span></span>, Demi-dragon
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">01/11/2011
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Singed" title="Singed"><img alt="SingedPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d6/SingedPortrait.png/revision/latest/scale-to-width-down/20?cb=20141011121548&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SingedPortrait.png" data-image-key="SingedPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/d6/SingedPortrait.png/revision/latest/scale-to-width-down/20?cb=20141011121548&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Singed" title="Singed">Singed</a></span></span>, Chimiste fou
</td>
<td bgcolor="#242424">Tank
</td>
<td>Top
</td>
<td bgcolor="#242424">18/04/2009
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Sion" title="Sion"><img alt="SionPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/5/5d/SionPortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223516&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SionPortrait.png" data-image-key="SionPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/5/5d/SionPortrait.png/revision/latest/scale-to-width-down/20?cb=20150107223516&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Sion" title="Sion">Sion</a></span></span>, Colosse mort-vivant
</td>
<td bgcolor="#242424">Tank
</td>
<td>Top
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Sivir" title="Sivir"><img alt="SivirPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/01/SivirPortrait.png/revision/latest/scale-to-width-down/20?cb=20240916193722&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SivirPortrait.png" data-image-key="SivirPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/01/SivirPortrait.png/revision/latest/scale-to-width-down/20?cb=20240916193722&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Sivir" title="Sivir">Sivir</a></span></span>, Vierge martiale
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Skarner" title="Skarner"><img alt="SkarnerPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/6/6e/SkarnerPortrait.png/revision/latest/scale-to-width-down/20?cb=20240916193828&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SkarnerPortrait.png" data-image-key="SkarnerPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/6/6e/SkarnerPortrait.png/revision/latest/scale-to-width-down/20?cb=20240916193828&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Skarner" title="Skarner">Skarner</a></span></span>, Gardien de cristal
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">09/08/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Smolder" title="Smolder"><img alt="SmolderPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/3/37/SmolderPortrait.png/revision/latest/scale-to-width-down/20?cb=20240131190906&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SmolderPortrait.png" data-image-key="SmolderPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/3/37/SmolderPortrait.png/revision/latest/scale-to-width-down/20?cb=20240131190906&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><span class="new" title="Smolder (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvU21vbGRlcj9hY3Rpb249ZWRpdCZyZWRsaW5rPTE=">Smolder</span></span></span>, Dragonnet flamboyant
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">31/01/2024
</td>
<td bgcolor="#242424">7800
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Sona" title="Sona"><img alt="SonaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/6/66/SonaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150204133046&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SonaPortrait.png" data-image-key="SonaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/6/66/SonaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150204133046&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Sona" title="Sona">Sona</a></span></span>, Virtuose de la harpe
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">21/09/2010
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Soraka" title="Soraka"><img alt="SorakaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/5/51/SorakaPortrait.png/revision/latest/scale-to-width-down/20?cb=20120921041346&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SorakaPortrait.png" data-image-key="SorakaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/5/51/SorakaPortrait.png/revision/latest/scale-to-width-down/20?cb=20120921041346&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Soraka" title="Soraka">Soraka</a></span></span>, Enfant des étoiles
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Swain" title="Swain"><img alt="SwainPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4b/SwainPortrait.png/revision/latest/scale-to-width-down/20?cb=20180222170435&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SwainPortrait.png" data-image-key="SwainPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4b/SwainPortrait.png/revision/latest/scale-to-width-down/20?cb=20180222170435&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Swain" title="Swain">Swain</a></span></span>, Grand général noxien
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">05/10/2010
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align: left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Sylas" title="Sylas"><img alt="SylasPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/3/39/SylasPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712172924&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SylasPortrait.png" data-image-key="SylasPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/3/39/SylasPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712172924&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Sylas" title="Sylas">Sylas</a></span></span>, Révolutionnaire déchaîné
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">25/01/2019
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Syndra" title="Syndra"><img alt="SyndraPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/2/23/SyndraPortrait.png/revision/latest/scale-to-width-down/20?cb=20240916193937&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="SyndraPortrait.png" data-image-key="SyndraPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/2/23/SyndraPortrait.png/revision/latest/scale-to-width-down/20?cb=20240916193937&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Syndra" title="Syndra">Syndra</a></span></span>, Souveraine obscure
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">13/09/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Tahm_Kench" title="Tahm Kench"><img alt="TahmKenchPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/3/3d/Tahm_KenchPortrait.png/revision/latest/scale-to-width-down/20?cb=20150624113831&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="Tahm KenchPortrait.png" data-image-key="Tahm_KenchPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/3/3d/Tahm_KenchPortrait.png/revision/latest/scale-to-width-down/20?cb=20150624113831&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Tahm_Kench" title="Tahm Kench">Tahm Kench</a></span></span>, Roi des rivières
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">09/07/2015
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Taliyah" title="Taliyah"><img alt="TaliyahPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/c/ca/TaliyahPortrait.png/revision/latest/scale-to-width-down/20?cb=20170115125948&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="TaliyahPortrait.png" data-image-key="TaliyahPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/c/ca/TaliyahPortrait.png/revision/latest/scale-to-width-down/20?cb=20170115125948&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Taliyah" title="Taliyah">Taliyah</a></span></span>, Tisseuse de pierres
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">18/05/2016
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Talon" title="Talon"><img alt="TalonPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/a/ae/TalonPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213606&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="TalonPortrait.png" data-image-key="TalonPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/a/ae/TalonPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213606&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Talon" title="Talon">Talon</a></span></span>, Lame des ténèbres
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Jungle
</td>
<td bgcolor="#242424">24/08/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Taric" title="Taric"><img alt="TaricPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/2/23/TaricPortrait.png/revision/latest/scale-to-width-down/20?cb=20160425192846&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="TaricPortrait.png" data-image-key="TaricPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/2/23/TaricPortrait.png/revision/latest/scale-to-width-down/20?cb=20160425192846&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Taric" title="Taric">Taric</a></span></span>, Bouclier de Valoran
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">19/08/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Teemo" title="Teemo"><img alt="TeemoPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4f/TeemoPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630032256&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="TeemoPortrait.png" data-image-key="TeemoPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4f/TeemoPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630032256&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Teemo" title="Teemo">Teemo</a></span></span>, Scout de Bantam
</td>
<td bgcolor="#242424">Tireur
</td>
<td>Top
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Thresh" title="Thresh"><img alt="ThreshPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/3/3f/ThreshPortrait.png/revision/latest/scale-to-width-down/20?cb=20130110024026&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ThreshPortrait.png" data-image-key="ThreshPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/3/3f/ThreshPortrait.png/revision/latest/scale-to-width-down/20?cb=20130110024026&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Thresh" title="Thresh">Thresh</a></span></span>, Garde aux chaînes
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">23/01/2013
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Tristana" title="Tristana"><img alt="TristanaPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/5/55/TristanaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150218221554&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="TristanaPortrait.png" data-image-key="TristanaPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/5/55/TristanaPortrait.png/revision/latest/scale-to-width-down/20?cb=20150218221554&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Tristana" title="Tristana">Tristana</a></span></span>, Cannonière yordle
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Trundle" title="Trundle"><img alt="TrundlePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f9/TrundlePortrait.png/revision/latest/scale-to-width-down/20?cb=20130404053351&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="TrundlePortrait.png" data-image-key="TrundlePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f9/TrundlePortrait.png/revision/latest/scale-to-width-down/20?cb=20130404053351&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Trundle" title="Trundle">Trundle</a></span></span>, Roi des trolls
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">01/12/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Tryndamere" title="Tryndamere"><img alt="TryndamerePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/1/11/TryndamerePortrait.png/revision/latest/scale-to-width-down/20?cb=20120908055238&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="TryndamerePortrait.png" data-image-key="TryndamerePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/1/11/TryndamerePortrait.png/revision/latest/scale-to-width-down/20?cb=20120908055238&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Tryndamere" title="Tryndamere">Tryndamere</a></span></span>, Roi barbare
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">01/05/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Twisted_Fate" title="Twisted Fate"><img alt="TwistedFatePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/db/TwistedFatePortrait.png/revision/latest/scale-to-width-down/20?cb=20121005001157&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="TwistedFatePortrait.png" data-image-key="TwistedFatePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/db/TwistedFatePortrait.png/revision/latest/scale-to-width-down/20?cb=20121005001157&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Twisted_Fate" title="Twisted Fate">Twisted Fate</a></span></span>, Maître des cartes
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Twitch" title="Twitch"><img alt="TwitchPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/8/8a/TwitchPortrait.png/revision/latest/scale-to-width-down/20?cb=20140412060306&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="TwitchPortrait.png" data-image-key="TwitchPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/8/8a/TwitchPortrait.png/revision/latest/scale-to-width-down/20?cb=20140412060306&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Twitch" title="Twitch">Twitch</a></span></span>, Semeur de peste
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">01/05/2009
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Udyr" title="Udyr"><img alt="UdyrPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4b/UdyrPortrait.png/revision/latest/scale-to-width-down/20?cb=20220928161730&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="UdyrPortrait.png" data-image-key="UdyrPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4b/UdyrPortrait.png/revision/latest/scale-to-width-down/20?cb=20220928161730&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Udyr" title="Udyr">Udyr</a></span></span>, Gardien des esprits
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">02/12/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Urgot" title="Urgot"><img alt="UrgotPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/f/fe/UrgotPortrait.png/revision/latest/scale-to-width-down/20?cb=20180220223912&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="UrgotPortrait.png" data-image-key="UrgotPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/f/fe/UrgotPortrait.png/revision/latest/scale-to-width-down/20?cb=20180220223912&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Urgot" title="Urgot">Urgot</a></span></span>, Broyeur
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">24/08/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Varus" title="Varus"><img alt="VarusPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c3/VarusPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712173000&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="VarusPortrait.png" data-image-key="VarusPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/c/c3/VarusPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712173000&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Varus" title="Varus">Varus</a></span></span>, Flèche de la vengeance
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">08/05/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Vayne" title="Vayne"><img alt="VaynePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/6/6b/VaynePortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213649&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="VaynePortrait.png" data-image-key="VaynePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/6/6b/VaynePortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213649&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Vayne" title="Vayne">Vayne</a></span></span>, Chasseresse nocturne
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">10/05/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Veigar" title="Veigar"><img alt="VeigarPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/73/VeigarPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213657&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="VeigarPortrait.png" data-image-key="VeigarPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/73/VeigarPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213657&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Veigar" title="Veigar">Veigar</a></span></span>, Seigneur des maléfices
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">24/07/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Vel%27Koz" title="Vel'Koz"><img alt="VelKozPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/6/6b/Vel%27KozPortrait.png/revision/latest/scale-to-width-down/20?cb=20140212004835&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="Vel'KozPortrait.png" data-image-key="Vel%27KozPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/6/6b/Vel%27KozPortrait.png/revision/latest/scale-to-width-down/20?cb=20140212004835&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Vel%27Koz" title="Vel'Koz">Vel'Koz</a></span></span>, Œil du Néant
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">27/02/2014
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Vex" title="Vex"><img alt="VexPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/46/VexPortrait.png/revision/latest/scale-to-width-down/20?cb=20220711124308&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="VexPortrait.png" data-image-key="VexPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/46/VexPortrait.png/revision/latest/scale-to-width-down/20?cb=20220711124308&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><span class="new" title="Vex (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvVmV4P2FjdGlvbj1lZGl0JnJlZGxpbms9MQ==">Vex</span></span></span>, Yordle sinistre
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">23/09/2021
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Vi" title="Vi"><img alt="ViPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/5/50/ViPortrait.png/revision/latest/scale-to-width-down/20?cb=20121212053845&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ViPortrait.png" data-image-key="ViPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/5/50/ViPortrait.png/revision/latest/scale-to-width-down/20?cb=20121212053845&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Vi" title="Vi">Vi</a></span></span>, Cogne de Piltover
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">19/12/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Viego" title="Viego"><img alt="ViegoPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/74/ViegoPortrait.png/revision/latest/scale-to-width-down/20?cb=20220927190150&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ViegoPortrait.png" data-image-key="ViegoPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/74/ViegoPortrait.png/revision/latest/scale-to-width-down/20?cb=20220927190150&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><span class="new" title="Viego (page inexistante)" data-uncrawlable-url="L2ZyL3dpa2kvVmllZ28/YWN0aW9uPWVkaXQmcmVkbGluaz0x">Viego</span></span></span>, Roi déchu
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Jungle
</td>
<td bgcolor="#242424">21/01/2021
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Viktor" title="Viktor"><img alt="ViktorPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a9/ViktorPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213705&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ViktorPortrait.png" data-image-key="ViktorPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a9/ViktorPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213705&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Viktor" title="Viktor">Viktor</a></span></span>, Héraut des machines
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">29/12/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Vladimir" title="Vladimir"><img alt="VladimirPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/9/9e/VladimirPortrait.png/revision/latest/scale-to-width-down/20?cb=20121022095117&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="VladimirPortrait.png" data-image-key="VladimirPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/9/9e/VladimirPortrait.png/revision/latest/scale-to-width-down/20?cb=20121022095117&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Vladimir" title="Vladimir">Vladimir</a></span></span>, Saigneur pourpre
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">27/07/2010
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Volibear" title="Volibear"><img alt="VolibearPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f2/VolibearPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712173025&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="VolibearPortrait.png" data-image-key="VolibearPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/f/f2/VolibearPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712173025&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Volibear" title="Volibear">Volibear</a></span></span>, Tempête impitoyable
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">29/11/2011
</td>
<td bgcolor="#242424">3150
</td>
<td bgcolor="#242424">790
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Warwick" title="Warwick"><img alt="WarwickPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/d/da/WarwickPortrait.png/revision/latest/scale-to-width-down/20?cb=20170112222127&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="WarwickPortrait.png" data-image-key="WarwickPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/d/da/WarwickPortrait.png/revision/latest/scale-to-width-down/20?cb=20170112222127&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Warwick" title="Warwick">Warwick</a></span></span>, Fureur déchainée de Zaun
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">21/02/2009
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">260
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Wukong" title="Wukong"><img alt="WukongPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/0/03/WukongPortrait.png/revision/latest/scale-to-width-down/20?cb=20141030234258&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="WukongPortrait.png" data-image-key="WukongPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/0/03/WukongPortrait.png/revision/latest/scale-to-width-down/20?cb=20141030234258&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Wukong" title="Wukong">Wukong</a></span></span>, Roi des singes
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">26/07/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Xayah" title="Xayah"><img alt="XayahPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/2/2f/XayahPortrait.png/revision/latest/scale-to-width-down/20?cb=20170405212320&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="XayahPortrait.png" data-image-key="XayahPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/2/2f/XayahPortrait.png/revision/latest/scale-to-width-down/20?cb=20170405212320&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Xayah" title="Xayah">Xayah</a></span></span>, Rebelle
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">19/04/2017
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Xerath" title="Xerath"><img alt="XerathPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/a/ac/XerathPortrait.png/revision/latest/scale-to-width-down/20?cb=20170103203045&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="XerathPortrait.png" data-image-key="XerathPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/a/ac/XerathPortrait.png/revision/latest/scale-to-width-down/20?cb=20170103203045&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Xerath" title="Xerath">Xerath</a></span></span>, Mage suprême
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">05/10/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Xin_Zhao" title="Xin Zhao"><img alt="XinZhaoPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4d/XinZhaoPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712173119&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="XinZhaoPortrait.png" data-image-key="XinZhaoPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/4/4d/XinZhaoPortrait.png/revision/latest/scale-to-width-down/20?cb=20200712173119&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Xin_Zhao" title="Xin Zhao">Xin Zhao</a></span></span>, Sénéchal de Demacia
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Jungle
</td>
<td bgcolor="#242424">13/07/2010
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Yasuo" title="Yasuo"><img alt="YasuoPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a1/YasuoPortrait.png/revision/latest/scale-to-width-down/20?cb=20131127221956&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="YasuoPortrait.png" data-image-key="YasuoPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a1/YasuoPortrait.png/revision/latest/scale-to-width-down/20?cb=20131127221956&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Yasuo" title="Yasuo">Yasuo</a></span></span>, Disgracié
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Mid
</td>
<td bgcolor="#242424">13/12/2013
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Yone" title="Yone"><img alt="YonePortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a6/YonePortrait.png/revision/latest/scale-to-width-down/20?cb=20220711124321&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="YonePortrait.png" data-image-key="YonePortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a6/YonePortrait.png/revision/latest/scale-to-width-down/20?cb=20220711124321&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Yone" title="Yone">Yone</a></span></span>, Inoublié
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Mid
</td>
<td bgcolor="#242424">06/08/2020
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Yorick" title="Yorick"><img alt="YorickPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/f/fc/YorickPortrait.png/revision/latest/scale-to-width-down/20?cb=20170115130102&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="YorickPortrait.png" data-image-key="YorickPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/f/fc/YorickPortrait.png/revision/latest/scale-to-width-down/20?cb=20170115130102&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Yorick" title="Yorick">Yorick</a></span></span>, Berger des âmes
</td>
<td bgcolor="#242424">Combattant
</td>
<td>Top
</td>
<td bgcolor="#242424">22/06/2011
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Yuumi" title="Yuumi"><img alt="YuumiPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/9/91/YuumiPortrait.png/revision/latest/scale-to-width-down/20?cb=20190902130320&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="YuumiPortrait.png" data-image-key="YuumiPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/9/91/YuumiPortrait.png/revision/latest/scale-to-width-down/20?cb=20190902130320&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Yuumi" title="Yuumi">Yuumi</a></span></span>, Gardienne du Grimoire
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">14/05/2019
</td>
<td bgcolor="#242424">450
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Zac" title="Zac"><img alt="ZacPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/9/97/ZacPortrait.png/revision/latest/scale-to-width-down/20?cb=20130316031941&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ZacPortrait.png" data-image-key="ZacPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/9/97/ZacPortrait.png/revision/latest/scale-to-width-down/20?cb=20130316031941&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Zac" title="Zac">Zac</a></span></span>, Arme secrète
</td>
<td bgcolor="#242424">Tank
</td>
<td>Jungle
</td>
<td bgcolor="#242424">29/03/2013
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Zed" title="Zed"><img alt="ZedPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/2/22/ZedPortrait.png/revision/latest/scale-to-width-down/20?cb=20121102025318&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ZedPortrait.png" data-image-key="ZedPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/2/22/ZedPortrait.png/revision/latest/scale-to-width-down/20?cb=20121102025318&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Zed" title="Zed">Zed</a></span></span>, Maître des ombres
</td>
<td bgcolor="#242424">Assassin
</td>
<td>Mid
</td>
<td bgcolor="#242424">13/11/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Zeri" title="Zeri"><img alt="ZeriPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a2/ZeriPortrait.png/revision/latest/scale-to-width-down/20?cb=20220927190220&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ZeriPortrait.png" data-image-key="ZeriPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/a/a2/ZeriPortrait.png/revision/latest/scale-to-width-down/20?cb=20220927190220&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Zeri" title="Zeri">Zeri</a></span></span>, Étincelle de Zaun
</td>
<td bgcolor="#242424">Tireur
</td>
<td>ADC
</td>
<td bgcolor="#242424">20/01/2022
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Ziggs" title="Ziggs"><img alt="ZiggsPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/1/1d/ZiggsPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630032932&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ZiggsPortrait.png" data-image-key="ZiggsPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/1/1d/ZiggsPortrait.png/revision/latest/scale-to-width-down/20?cb=20120630032932&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Ziggs" title="Ziggs">Ziggs</a></span></span>, Expert des Hexplosifs
</td>
<td bgcolor="#242424">Mage
</td>
<td>ADC
</td>
<td bgcolor="#242424">01/02/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Zilean" title="Zilean"><img alt="ZileanPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/1/1e/ZileanPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213713&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ZileanPortrait.png" data-image-key="ZileanPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/1/1e/ZileanPortrait.png/revision/latest/scale-to-width-down/20?cb=20150105213713&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Zilean" title="Zilean">Zilean</a></span></span>, Gardien du Temps
</td>
<td bgcolor="#242424">Support
</td>
<td>Support
</td>
<td bgcolor="#242424">18/04/2009
</td>
<td bgcolor="#242424">1350
</td>
<td bgcolor="#242424">585
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Zo%C3%A9" title="Zoé"><img alt="ZoéPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/7/72/Zo%C3%A9Portrait.png/revision/latest/scale-to-width-down/20?cb=20180211143559&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ZoéPortrait.png" data-image-key="Zo%C3%A9Portrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/7/72/Zo%C3%A9Portrait.png/revision/latest/scale-to-width-down/20?cb=20180211143559&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Zo%C3%A9" title="Zoé">Zoé</a></span></span>, Manifestation du Crépuscule
</td>
<td bgcolor="#242424">Mage
</td>
<td>Mid
</td>
<td bgcolor="#242424">21/11/2017
</td>
<td bgcolor="#242424">6300
</td>
<td bgcolor="#242424">975
</td></tr>
<tr>
<td style="text-align:left;" bgcolor="#242424"><span class="character_icon"><a href="/fr/wiki/Zyra" title="Zyra"><img alt="ZyraPortrait" src="https://static.wikia.nocookie.net/leagueoflegends/images/8/8f/ZyraPortrait.png/revision/latest/scale-to-width-down/20?cb=20120714162422&amp;path-prefix=fr" decoding="async" loading="lazy" width="20" height="20" data-image-name="ZyraPortrait.png" data-image-key="ZyraPortrait.png" data-relevant="0" data-src="https://static.wikia.nocookie.net/leagueoflegends/images/8/8f/ZyraPortrait.png/revision/latest/scale-to-width-down/20?cb=20120714162422&amp;path-prefix=fr" class=" ls-is-cached lazyloaded"></a> <span><a href="/fr/wiki/Zyra" title="Zyra">Zyra</a></span></span>, Dame aux ronces
</td>
<td bgcolor="#242424">Mage
</td>
<td>Support
</td>
<td bgcolor="#242424">24/07/2012
</td>
<td bgcolor="#242424">4800
</td>
<td bgcolor="#242424">880
</td></tr></tbody><tfoot></tfoot></table>
"""

if __name__ == '__main__':
    soup = BeautifulSoup(html, 'html.parser')
    table_table = soup.find('table')
    rows_tr = table_table.find_all('tr')[1:]

    data = []
    for row in rows_tr:
        row_td = row.find_all('td')

        name = row_td[0].find('a').get('title')
        lane = row_td[2].text.strip()
        date_release = row_td[3].text.strip()

        day, month, year = date_release.split('/')

        date_release = f'{year}-{month}-{day}'

        data.append([name, lane, date_release])

    df = pd.DataFrame(data, columns=['name', 'lane', 'date_release'])
    df.to_csv('champions_lane_and_date_release.csv', index=False)
