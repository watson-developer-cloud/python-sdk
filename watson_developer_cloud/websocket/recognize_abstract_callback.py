from abc import abstractmethod, ABCMeta

class RecognizeAbstractCallback:
  __metaclass__ = ABCMeta

  """
  Called when an interim result is received
  """
  @abstractmethod
  def on_transcription(self, transcript):
    pass

  """
  Called when a WebSocket connection was made
  """
  @abstractmethod
  def on_connected(self):
    pass

  """
  Called when there is an error in the Web Socket connection.
  """
  @abstractmethod
  def on_error(self, error):
    pass

  """
  Called when there is an inactivity timeout.
  """
  @abstractmethod
  def on_inactivity_timeout(self):
    pass

  """
  Called when the service is listening for audio.
  """
  @abstractmethod
  def on_listening(self):
    pass

  """
  Called after the service returns the final result for the transcription.
  """
  @abstractmethod
  def on_transcription_complete(self):
    pass

  """
  Called when the service returns the final hypothesis
  """
  def on_hypothesis(self, hypothesis):
    pass