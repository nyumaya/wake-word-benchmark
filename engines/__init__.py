#
# Copyright 2018 Picovoice Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
import sys

# Add Porcupine's binding file to the system path.
sys.path.append(os.path.join(os.path.dirname(__file__), 'porcupine/binding/python'))
# Add Snowboy's binding file to the system path.
if sys.version_info[0] < 3:
    sys.path.append(os.path.join(os.path.dirname(__file__), 'snowboy/swig/Python'))
else:
    sys.path.append(os.path.join(os.path.dirname(__file__), 'snowboy/swig/Python3'))

from porcupine import Porcupine
import snowboydetect

sys.path.append(os.path.join(os.path.dirname(__file__), 'nyumaya_audio_recognition/python/src'))

from libnyumaya import AudioRecognition, FeatureExtractor
