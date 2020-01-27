import panas as pd
import numpy as np


url =
"https://raw.githubusercontent.com/AnnaReyc/machineLearning/master/aritmya_new.csv"
names = ['Age', 'Sex', 'Height', 'Weight', 'QRS duration', 'P-R interval', 'Q-T
interval', 'T interval', 'P interval', 'QRS', 'T', 'P', 'QRST', 'J', 'Heart rate', 'Q
wave I', 'R wave I', 'S wave I', I', 'Number of intrinsic
deflections I', 'Existence of ragged R wave I', 'Existence of diphasic derivation
of R wave I', 'Existence of ragged P wave I', 'Existence of diphasic derivation
of P wave I', 'Existence of ragged T wave I', 'Existence of diphasic derivation
of T wave I', 'Q wave II', 'R wave II', 'S wave II', II',
II', 'Number of intrinsic deflections II', 'Existence of ragged R wave II',
'Existence of diphasic derivation of R wave II', 'Existence of ragged P wave,
nominal II', 'Existence of diphasic derivation of P wave II', 'Existence of
ragged T wave II', 'Existence of diphasic derivation of T wave II', 'Q wave
III', 'R wave III', 'S wave III', III', III', 'Number of
intrinsic deflections III', 'Existence of ragged R wave III', 'Existence of
diphasic derivation of R wave III', 'Existence of ragged P wave, nominal III',
'Existence of diphasic derivation of P wave III', 'Existence of ragged T wave
III', 'Existence of diphasic derivation of T wave III', 'Q wave AVR', 'R wave
AVR', 'S wave AVR', AVR', AVR', 'Number of intrinsic
deflections - AVR', 'Existence of ragged R wave AVR', 'Existence of diphasic
derivation of R wave AVR', 'Existence of ragged P wave AVR', 'Existence of
diphasic derivation of P wave AVR', 'Existence of ragged T wave AVR', 'Existence
of diphasic derivation of T wave AVR', 'Q wave AVL', 'R wave AVL', 'S wave
AVL', AVL', 'Existence of ragged R wave AVL', 'Existence of diphasic
derivation of R wave AVL', 'Existence of ragged P wave, nominal AVL', 'Existence
of diphasic derivation of P wave AVL', 'Existence of ragged T wave AVL',
'Existence of diphasic derivation of T wave AVL', 'Q wave AVF', 'R wave AVF',
'S wave AVF', AVF', AVF', 'Number of intrinsic deflections -
AVF', 'Existence of ragged R wave AVF', 'Existence of diphasic derivation of R wave
AVF', 'Existence of diphasic derivation of P wave AVF', 'Existence of ragged T
wave AVF', 'Existence of diphasic derivation of T wave AVF', 'Q wave V1', 'R
wave V1', 'S wave V1', V1', V1', 'Number of intrinsic
deflections - V1', 'Existence of ragged R wave V1', 'Existence of diphasic
derivation of R wave V1', 'Existence of ragged P wave, nominal V1', 'Existence of
diphasic derivation of P wave V1', 'Existence of ragged T wave V1', 'Existence of
diphasic derivation of T wave V1', 'Q wave V2', 'R wave V2', 'S wave V2',
wave V2', V2', 'Number of intrinsic deflections - V2', 'Existence of
ragged R wave V2', 'Existence of diphasic derivation of R wave V2', 'Existence of
ragged P wave, nominal V2', 'Existence of diphasic derivation of P wave V2',
'Existence of ragged T wave V2', 'Existence of diphasic derivation of T wave V2',
'Q wave V3', 'R wave V3', 'S wave V3', V3', V3', 'Number
of intrinsic deflections - V3', 'Existence of ragged R wave V3', 'Existence of
diphasic derivation of R wave V3', 'Existence of ragged P wave, nominal V3',
'Existence of diphasic derivation of P wave V3', 'Existence of ragged T wave V3', 
66
'Existence of diphasic derivation of T wave V3', 'Q wave V4', 'R wave V4', 'S
wave V4', V4', V4', 'Number of intrinsic deflections - V4',
'Existence of ragged R wave V4', 'Existence of diphasic derivation of R wave V4',
'Existence of ragged T wave V4', 'Existence of diphasic derivation of T wave V4',
'Q wave V5', 'R wave V5', 'S wave V5', V5', 'Number of intrinsic
deflections - V5', 'Existence of diphasic derivation of R wave V5', 'Existence of
diphasic derivation of P wave V5', 'Existence of ragged T wave V5', 'Q wave
V6', 'R wave V6', 'S wave V6', V6', 'Number of intrinsic deflections -
V6', 'Existence of ragged R wave V6', 'Existence of diphasic derivation of R wave
V6', 'Existence of ragged P wave, nominal V6', 'Existence of diphasic derivation of
P wave V6', 'Existence of ragged T wave V6', 'Existence of diphasic derivation of
T wave V6', 'JJ wave amplitude I', 'Q wave amplitude I', 'R wave amplitude
I', 'S wave amplitude I', I', I', 'P wave
amplitude I', 'T wave amplitude I', 'QRSA I', 'QRSTA I', 'JJ wave amplitude
II', 'Q wave amplitude II', 'R wave amplitude II', 'S wave amplitude II',
wave amplitude II', II', 'P wave amplitude II', 'T wave
amplitude II', 'QRSA II', 'QRSTA II', 'JJ wave amplitude III', 'Q wave
amplitude III', 'R wave amplitude III', 'S wave amplitude III',
amplitude III', ve amplitude III', 'P wave amplitude III', 'T wave
amplitude III', 'QRSA III', 'QRSTA III', 'JJ wave amplitude AVR', 'Q wave
amplitude AVR', 'R wave amplitude AVR', 'S wave amplitude AVR',
amplitude AVR', AVR', 'P wave amplitude AVR', 'T wave
amplitude AVR', 'QRSA AVR', 'QRSTA AVR', 'JJ wave amplitude AVL', 'Q wave
amplitude AVL', 'R wave amplitude AVL', 'S wave amplitude AVL',
amplitude AVL', AVL', 'P wave amplitude AVL', 'T wave
amplitude AVL', 'QRSA AVL', 'QRSTA AVL', 'JJ wave amplitude AVF', 'Q wave
amplitude AVF', 'R wave amplitude AVF', 'S wave amplitude AVF',
amplitude AVF', AVF', 'P wave amplitude AVF', 'T wave
amplitude AVF', 'QRSA AVF', 'QRSTA AVF', 'JJ wave amplitude V1', 'Q wave
amplitude V1', 'R wave amplitude V1', 'S wave amplitude V1',
V1', V1', 'P wave amplitude V1', 'T wave amplitude V1',
'QRSA V1', 'QRSTA V1', 'JJ wave amplitude V2', 'Q wave amplitude V2', 'R wave
amplitude V2', 'S wave amplitude V2', V2',
amplitude V2', 'P wave amplitude V2', 'T wave amplitude V2', 'QRSA V2',
'QRSTA V2','JJ wave amplitude V3', 'Q wave amplitude V3', 'R wave amplitude
V3', 'S wave amplitude V3', V3', V3', 'P
wave amplitude V3', 'T wave amplitude V3', 'QRSA V3', 'QRSTA V3', 'JJ wave
amplitude V4', 'Q wave amplitude V4', 'R wave amplitude V4', 'S wave amplitude
V4', V4', V4', 'P wave amplitude V4',
'T wave amplitude V4', 'QRSA V4', 'QRSTA V4','JJ wave amplitude V5', 'Q wave
amplitude V5', 'R wave amplitude V5', 'S wave amplitude V5',
V5', V5', 'P wave amplitude V5', 'T wave amplitude V5',
'QRSA V5', 'QRSTA V5', 'JJ wave amplitude V6', 'Q wave amplitude V6', 'R wave
amplitude V6', 'S wave amplitude V6', V6', 'P wave amplitude
V6', 'T wave amplitude V6', 'QRSA V6', 'QRSTA V6','class']

dataset = pandas.read_csv(url, names=names)
dataset = dataset.replace({'?': '0'}) #заменили все ? на 0 

for col in list(dataset.columns):
  if ('J' in col or 'Heart rate' in col or 'P' in col or 'T' in col or 'QRST' in
col):
  dataset[col] = dataset[col].astype(int) #преобразование столбцов с типом object в int
  
data=dataset[dataset.columns.difference(['class'])]
target=dataset['class']
