#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import html
from random import randint
import tweepy
import requests
import js2py
import urllib
import time
import encodings

# first you must create a twitter application on enter the corresponding https://apps.twitter.com/
# under tab 'Keys and Access tokens' generate 'Consumer Key and Secret' and 'Access Token and Token Secret'
# copy your keys Twitter application:
CONSUMER_KEY = '...'  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '...'  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '...'  # keep the quotes, replace this with your access token
ACCESS_SECRET = '...'  # keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def capitalizeFirstLetter(str):
	return str.capitalize()

def generateSentence(topic):
	sentencePool = list(sentencePatterns)
	patternNumber = randint(0,len(sentencePool) - 1)
	pattern = sentencePool[topic][patternNumber]

	#insert a space before . , ; ? so we can split the string into an array
	pattern = insertSpaceBeforePunctuation(pattern)
	pattern = pattern.split(' ')

	#remove the pattern from the sentence pool so it can't be re-used
	sentencePool[topic].pop(patternNumber)

	#remove the topic from the sentence pool if there are no sentences left
	#for that particular topic
	if len(sentencePool[topic]) == 0:
		sentencePool.pop(topic)


	result = ''
	for x in pattern:
		#if word matches one of the placeholder words (e.g. nPerson),
		#replace it with a random instance of its type (e.g. warrior)
		if x in bullshitWords:
			result += bullshitWords[x][randint(0,len(bullshitWords[x])-1)]
		else:
			result += x
		result += ' '

	result = addSpaceAfterQuestionMarks(deleteSpaceAfterHyphen(removeSpacesBeforePunctuation(capitalizeFirstLetter(trim(replaceAWithAn(result))))))

	return result

def generateText(numberOfSentences, sentenceTopic):
	text = ''
	c = 0
	while c < numberOfSentences:
		text += generateSentence(sentenceTopic)
		c += 1

	text = insertSpaceBetweenSentences(text)
	text = replaceiWithI(text)

	return text
	
bullshitWords = {
	'nCosmos': [
		'cosmos',
		'quantum soup',
		'infinite',
		'universe',
		'galaxy',
		'multiverse',
		'grid',
		'quantum matrix',
		'totality',
		'quantum cycle',
		'nexus',
		'planet',
		'solar system',
		'world',
		'stratosphere',
		'dreamscape',
		'biosphere',
		'dreamtime'
	],

	'nPerson': [
		'being',
		'child',
		'traveller',
		'entity',
		'lifeform',
		'wanderer',
		'visitor',
		'prophet',
		'seeker',
		'Indigo Child'
	],

	'nPersonPlural': [
		'beings',
		'travellers',
		'entities',
		'lifeforms',
		'dreamweavers',
		'adventurers',
		'pilgrims',
		'warriors',
		'messengers',
		'dreamers',
		'storytellers',
		'seekers',
		'spiritual brothers and sisters',
		'mystics',
		'starseeds'
	],

	'nMass': [
		'consciousness',
		'nature',
		'beauty',
		'knowledge',
		'truth',
		'life',
		'healing',
		'potential',
		'freedom',
		'purpose',
		'coherence',
		'choice',
		'passion',
		'understanding',
		'balance',
		'growth',
		'inspiration',
		'conscious living',
		'energy',
		'health',
		'spacetime',
		'learning',
		'being',
		'wisdom',
		'stardust',
		'sharing',
		'science',
		'curiosity',
		'hope',
		'wonder',
		'faith',
		'fulfillment',
		'peace',
		'rebirth',
		'self-actualization',
		'presence',
		'power',
		'will',
		'flow',
		'potentiality',
		'chi',
		'intuition',
		'synchronicity',
		'wellbeing',
		'joy',
		'love',
		'karma',
		'life-force',
		'awareness',
		'guidance',
		'transformation',
		'grace',
		'divinity',
		'non-locality',
		'inseparability',
		'interconnectedness',
		'transcendence',
		'empathy',
		'insight',
		'rejuvenation',
		'ecstasy',
		'aspiration',
		'complexity',
		'serenity',
		'intention',
		'gratitude',
		'starfire',
		'manna'
	],

	'nMassBad': [
		'turbulence',
		'pain',
		'suffering',
		'stagnation',
		'desire',
		'bondage',
		'greed',
		'selfishness',
		'ego',
		'dogma',
		'illusion',
		'delusion',
		'yearning',
		'discontinuity',
		'materialism'
	],

	'nOurPlural': [
		'souls',
		'lives',
		'dreams',
		'hopes',
		'bodies',
		'hearts',
		'brains',
		'third eyes',
		'essences',
		'chakras',
		'auras'
	],

	'nPath': [
		'circuit',
		'mission',
		'journey',
		'path',
		'quest',
		'vision quest',
		'story',
		'myth'
	],

	'nOf': [
		'quantum leap',
		'evolution',
		'spark',
		'lightning bolt',
		'reintegration',
		'vector',
		'rebirth',
		'revolution',
		'wellspring',
		'fount',
		'source',
		'fusion',
		'canopy',
		'flow',
		'network',
		'current',
		'transmission',
		'oasis',
		'quantum shift',
		'paradigm shift',
		'metamorphosis',
		'harmonizing',
		'reimagining',
		'rekindling',
		'unifying',
		'osmosis',
		'vision',
		'uprising',
		'explosion'
	],

	'ing': [
		'flowering',
		'unfolding',
		'blossoming',
		'awakening',
		'deepening',
		'refining',
		'maturing',
		'evolving',
		'summoning',
		'unveiling',
		'redefining',
		'condensing',
		'ennobling',
		'invocation'
	],

	'adj': [
		'enlightened',
		'zero-point',
		'quantum',
		'high-frequency',
		'Vedic',
		'non-dual',
		'conscious',
		'sentient',
		'sacred',
		'infinite',
		'primordial',
		'ancient',
		'powerful',
		'spiritual',
		'higher',
		'advanced',
		'internal',
		'sublime',
		'technological',
		'dynamic',
		'life-affirming',
		'sensual',
		'unrestricted',
		'ever-present',
		'endless',
		'ethereal',
		'astral',
		'cosmic',
		'spatial',
		'transformative',
		'unified',
		'non-local',
		'mystical',
		'divine',
		'self-aware',
		'magical',
		'amazing',
		'interstellar',
		'unlimited',
		'authentic',
		'angelic',
		'karmic',
		'psychic',
		'pranic',
		'consciousness-expanding',
		'perennial',
		'heroic',
		'archetypal',
		'mythic',
		'intergalatic',
		'holistic',
		'joyous',
		'eternal'
	],

	'adjBig': [
		'epic',
		'unimaginable',
		'colossal',
		'unfathomable',
		'magnificent',
		'enormous',
		'jaw-dropping',
		'ecstatic',
		'powerful',
		'untold',
		'astonishing',
		'incredible',
		'breathtaking',
		'staggering'
	],

	'adjWith': [
		'aglow with',
		'buzzing with',
		'beaming with',
		'full of',
		'overflowing with',
		'radiating',
		'bursting with',
		'electrified with'
	],

	'adjPrefix': [
		'ultra-',
		'supra-',
		'hyper-',
		'pseudo-'
	],

	'vtMass': [
		'inspire',
		'integrate',
		'ignite',
		'discover',
		'rediscover',
		'foster',
		'release',
		'manifest',
		'harmonize',
		'engender',
		'bring forth',
		'bring about',
		'create',
		'spark',
		'reveal',
		'generate',
		'leverage'
	],

	'vtPerson': [
		'enlighten',
		'inspire',
		'empower',
		'unify',
		'strengthen',
		'recreate',
		'fulfill',
		'change',
		'develop',
		'heal',
		'awaken',
		'synergize',
		'ground',
		'bless',
		'beckon'
	],

	'viPerson': [
		'exist',
		'believe',
		'grow',
		'live',
		'dream',
		'reflect',
		'heal',
		'vibrate',
		'self-actualize'
	],

	'vtDestroy': [
		'destroy',
		'eliminate',
		'shatter',
		'disrupt',
		'sabotage',
		'exterminate',
		'obliterate',
		'eradicate',
		'extinguish',
		'erase',
		'confront'
	],

	'nTheXOf': [
		'richness',
		'truth',
		'growth',
		'nature',
		'healing',
		'knowledge',
		'birth',
		'deeper meaning'
	],

	'ppPerson': [
		'awakened',
		're-energized',
		'recreated',
		'reborn',
		'guided',
		'aligned'
	],

	'ppThingPrep': [
		'enveloped in',
		'transformed into',
		'nurtured by',
		'opened by',
		'immersed in',
		'engulfed in',
		'baptized in'
	],

	'fixedAdvP': [
		'through non-local interactions',
		'inherent in nature',
		'at the quantum level',
		'at the speed of light',
		'of unfathomable proportions',
		'on a cosmic scale',
		'devoid of self',
		'of the creative act'
	],

	'fixedAdvPPlace': [
		'in this dimension',
		'outside time',
		'within the Godhead',
		'at home in the cosmos'
	],

	'fixedNP': [
		'expanding wave functions',
		'superpositions of possibilities',
		'electromagnetic forces',
		'electromagnetic resonance',
		'molecular structures',
		'atomic ionization',
		'electrical impulses',
		'a resonance cascade',
		'bio-electricity',
		'ultrasonic energy',
		'sonar energy',
		'vibrations',
		'frequencies',
		'four-dimensional superstructures',
		'ultra-sentient particles',
		'sub-atomic particles',
		'chaos-driven reactions',
		'supercharged electrons',
		'supercharged waveforms',
		'pulses',
		'transmissions',
		'morphogenetic fields',
		'bio-feedback',
		'meridians',
		'morphic resonance',
		'psionic wave oscillations'
	],

	'nSubject': [
		'alternative medicine',
		'astrology',
		'tarot',
		'crystal healing',
		'the akashic record',
		'feng shui',
		'acupuncture',
		'homeopathy',
		'aromatherapy',
		'ayurvedic medicine',
		'faith healing',
		'prayer',
		'astral projection',
		'Kabala',
		'reiki',
		'naturopathy',
		'numerology',
		'affirmations',
		'the Law of Attraction',
		'tantra',
		'breathwork'
	],

	'vOpenUp': [
		'open up',
		'give us access to',
		'enable us to access',
		'remove the barriers to',
		'clear a path toward',
		'let us access',
		'tap into',
		'align us with',
		'amplify our connection to',
		'become our stepping-stone to',
		'be a gateway to'
	],

	'vTraverse': [
		'traverse',
		'walk',
		'follow',
		'engage with',
		'go along',
		'roam',
		'navigate',
		'wander',
		'embark on'
	],

	'nameOfGod': [
		'Gaia',
		'Shiva',
		'Parvati',
		'the Goddess',
		'Shakti'
	],

	'nBenefits': [
		'improved focus',
		'improved concentration',
		'extreme performance',
		'enlightenment',
		'cellular regeneration',
		'an enhanced sexual drive',
		'improved hydration',
		'psychic rejuvenation',
		'a healthier relationship with the Self'
	],

	'adjProduct': [
		'alkaline',
		'quantum',
		'holographic',
		'zero-point energy',
		'living',
		'metaholistic',
		'ultraviolet',
		'ozonized',
		'ion-charged',
		'hexagonal-cell',
		'organic'
	],

	'nProduct': [
		'water',
		'healing crystals',
		'Tibetan singing bowls',
		'malachite runes',
		'meditation bracelets',
		'healing wands',
		'rose quartz',
		'karma bracelets',
		'henna tattoos',
		'hemp garments',
		'hemp seeds',
		'tofu',
		'massage oil',
		'herbal incense',
		'cheesecloth tunics'
	],
}

sentencePatterns = [

  # explaining
  [
	'nMass is the driver of nMass.',
	'nMass is the nTheXOf of nMass, and of us.',
	'You and I are nPersonPlural of the nCosmos.',
	'We exist as fixedNP.',
	'We viPerson, we viPerson, we are reborn.',
	'Nothing is impossible.',
	'This life is nothing short of a ing nOf of adj nMass.',
	'Consciousness consists of fixedNP of quantum energy. Quantum means a ing of the adj.',
	'The goal of fixedNP is to plant the seeds of nMass rather than nMassBad.',
	'nMass is a constant.',
	'By ing, we viPerson.',
	'The nCosmos is adjWith fixedNP.',
	'To vTraverse the nPath is to become one with it.',
	'Today, science tells us that the essence of nature is nMass.',
	'nMass requires exploration.',
  ],

  # warnings
  [
	'We can no longer afford to live with nMassBad.',
	'Without nMass, one cannot viPerson.',
	'Only a nPerson of the nCosmos may vtMass this nOf of nMass.',
	'You must take a stand against nMassBad.',
	'Yes, it is possible to vtDestroy the things that can vtDestroy us, but not without nMass on our side.',
	'nMassBad is the antithesis of nMass.',
	'You may be ruled by nMassBad without realizing it. Do not let it vtDestroy the nTheXOf of your nPath.',
	'The complexity of the present time seems to demand a ing of our nOurPlural if we are going to survive.',
	'nMassBad is born in the gap where nMass has been excluded.',
	'Where there is nMassBad, nMass cannot thrive.',
  ],

  # future hope
  [
	'Soon there will be a ing of nMass the likes of which the nCosmos has never seen.',
	'It is time to take nMass to the next level.',
	'Imagine a ing of what could be.',
	'Eons from now, we nPersonPlural will viPerson like never before as we are ppPerson by the nCosmos.',
	'It is a sign of things to come.',
	'The future will be a adj ing of nMass.',
	'This nPath never ends.',
	'We must learn how to lead adj lives in the face of nMassBad.',
	'We must vtPerson ourselves and vtPerson others.',
	'The nOf of nMass is now happening worldwide.',
	'We are being called to explore the nCosmos itself as an interface between nMass and nMass.',
	'It is in ing that we are ppPerson.',
	'The nCosmos is approaching a tipping point.',
	'nameOfGod will vOpenUp adj nMass.',
  ],

  # you and your problems
  [
	'Although you may not realize it, you are adj.',
	'nPerson, look within and vtPerson yourself.',
	'Have you found your nPath?',
	'How should you navigate this adj nCosmos?',
	'It can be difficult to know where to begin.',
	'If you have never experienced this nOf fixedAdvP, it can be difficult to viPerson.',
	'The nCosmos is calling to you via fixedNP. Can you hear it?',
  ],

  # history
  [
	'Throughout history, humans have been interacting with the nCosmos via fixedNP.',
	'Reality has always been adjWith nPersonPlural whose nOurPlural are ppThingPrep nMass.',
	'Our conversations with other nPersonPlural have led to a ing of adjPrefix adj consciousness.',
	'Humankind has nothing to lose.',
	'We are in the midst of a adj ing of nMass that will vOpenUp the nCosmos itself.',
	'Who are we? Where on the great nPath will we be ppPerson?',
	'We are at a crossroads of nMass and nMassBad.',
  ],

  # selling point
	[
	'Through nSubject, our nOurPlural are ppThingPrep nMass.',
	"nSubject may be the solution to what's holding you back from a adjBig nOf of nMass.",
	'You will soon be ppPerson by a power deep within yourself - a power that is adj, adj.',
	'As you viPerson, you will enter into infinite nMass that transcends understanding.',
	'This is the vision behind our 100% adjProduct, adjProduct nProduct.',
	'With our adjProduct nProduct, nBenefits is only the beginning.',
  ],

]

replaceAWithAn = js2py.eval_js(
	"""function replaceAWithAn(sentence) {
	return sentence.replace(/(^|\W)([Aa]) ([aeiou])/g, '$1$2n $3');
  }""")

removeSpacesBeforePunctuation = js2py.eval_js(
	"""function removeSpacesBeforePunctuation(sentence) {
	return sentence.replace(/ ([,\.;\?])/g, '$1');
  }""")

deleteSpaceAfterHyphen = js2py.eval_js(
	"""function deleteSpaceAfterHyphen(sentence) {
	return sentence.replace(/- /g, '-');
  }""")

addSpaceAfterQuestionMarks = js2py.eval_js(
	"""function addSpaceAfterQuestionMarks(sentence) {
	return sentence.replace(/\?(\w)/g, '? $1');
  }""")

insertSpaceBeforePunctuation = js2py.eval_js(
	"""function insertSpaceBeforePunctuation(sentence) {
	return sentence.replace(/([\.,;\?])/g, ' $1');
  }""")

insertSpaceBetweenSentences = js2py.eval_js(
	"""function insertSpaceBetweenSentences(text) {
	return text.replace(/([\.\?])(\w)/g, '$1 $2');
  }""")

replaceiWithI = js2py.eval_js(
	"""function replaceiWithI(text) {
	return text.replace(/( i )/, ' I ');
  }"""
)

trim = js2py.eval_js(
	"""function trim(text) {
	return text.trim();
  }""")

# repeat these steps in loop if you want to continuously tweet random bullshit

# get trending hashtags in United States from https://trends24.in/united-states/~cloud
tags_page = requests.get('https://trends24.in/united-states/~cloud')
tree = html.fromstring(tags_page.content)
usable_tags = []
tags = tree.xpath('//ol[@id="cloud-ol"]/li/a/text()')
for t in tags:
	if t[1] == '#':
		usable_tags.append(t)


topic = randint(0, len(sentencePatterns)-1)
numSen = 1
tag = randint(0,10)
ifImg = randint(0,1)
text = generateText(numSen,topic)
text += usable_tags[tag]

if ifImg == 1:
    # tweet with image
	urllib.urlretrieve("http://placeimg.com/640/480/nature", "pic.jpg")
	api.update_with_media("pic.jpg", text)
else:
    # tweet without image
	api.update_status(text)