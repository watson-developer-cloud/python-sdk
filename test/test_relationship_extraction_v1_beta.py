# coding=utf-8
import responses
import watson_developer_cloud


extract_response_body = '''
<?xml version='1.0' encoding='utf-8'?>
<rep sts="OK">
<doc id="">
  <text>Hello from IBM Watson</text>
  <sents>
    <sent sid="0" begin="0" end="3">
      <text>Hello from IBM Watson</text>
      <parse score="-4.13179">[FRAG [INTJ Hello_UH INTJ] [PP from_IN [NP IBM_NNP Watson_NNP NP] PP] FRAG]</parse>
      <dependency_parse>Hello UH 1 INTJ from IN -1 PP IBM NNP 3 -I Watson NNP 1 NP </dependency_parse>
      <usd_dependency_parse>Hello UH 1 discourse from IN 3 case IBM NNP 3 name Watson NNP -1 root</usd_dependency_parse>
      <tokens>
        <token tid="0" begin="0" end="4" type="0" POS="UH" lemma="hello">Hello</token>
        <token tid="1" begin="6" end="9" type="0" POS="IN" lemma="from">from</token>
        <token tid="2" begin="11" end="13" type="0" POS="NNP" lemma="ibm">IBM</token>
        <token tid="3" begin="15" end="20" type="4096" POS="NNP" lemma="watson">Watson</token>
      </tokens>
    </sent>
  </sents>
  <mentions>
    <mention mid="-M0" mtype="NAM" begin="11" end="20" head-begin="11" head-end="20" eid="-E0" etype="ORGANIZATION"
    role="ORGANIZATION" metonymy="0" class="SPC" score="0.963423" corefScore="1">IBM Watson</mention>
  </mentions>
  <entities>
    <entity eid="-E0" type="ORGANIZATION" generic="0" class="SPC" level="NAM" subtype="COMMERCIAL" score="1">
      <mentref mid="-M0">IBM Watson</mentref>
    </entity>
  </entities>
  <relations version="KLUE2_cascaded:2011_10_25"/>
  <sgml_sent_info/>
  <sgml_char_info/>
</doc></rep>
'''


@responses.activate
def test_success():
    extract_text = 'Hello from IBM Watson'
    extract_url = 'https://gateway.watsonplatform.net/relationship-extraction-beta/api/v1/sire/0'

    responses.add(responses.POST, extract_url,
                  body=extract_response_body, status=200,
                  content_type='application/xml')

    relationship_extraction = watson_developer_cloud.RelationshipExtractionV1Beta(
        username="username", password="password")
    relationship_extraction.extract(extract_text)

    assert responses.calls[0].request.url == extract_url
    assert responses.calls[0].response.text == extract_response_body
    assert len(responses.calls) == 1
