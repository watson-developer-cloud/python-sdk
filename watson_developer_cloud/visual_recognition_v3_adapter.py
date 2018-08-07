from .visual_recognition_v3 import VisualRecognitionV3

class VisualRecognitionV3Adapter(VisualRecognitionV3):
    def create_classifier(self,
                          name,
                          **kwargs):
        """
        Create a classifier.
        :param str name: The name of the new classifier. Encode special characters in UTF-8.
        :param file <NAME>_positive_examples: A compressed (.zip) file of images that depict the visual subject for a class within the new classifier. Include at least 10 images in .jpg or .png format. The minimum recommended image resolution is 32X32 pixels. The maximum number of images is 10,000 images or 100 MB per .zip file. Encode special characters in the file name in UTF-8.
        :param file negative_examples: A compressed (.zip) file of images that do not depict the visual subject of any of the classes of the new classifier. Must contain a minimum of 10 images. Encode special characters in the file name in UTF-8.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Classifier` response.
        :rtype: dict
        """
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {'name': name}
        url = '/v3/classifiers'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
            files=kwargs,
            accept_json=True)
        return response

    def update_classifier(self,
                          classifier_id,
                          **kwargs):
        """
        Update a classifier.
        :param str classifier_id: The ID of the classifier.
        :param file <NAME>_positive_examples: A .zip file of images that depict the visual subject of a class in the classifier. The positive examples create or update classes in the classifier. You can include more than one positive example file in a call. Include at least 10 images in .jpg or .png format. The minimum recommended image resolution is 32X32 pixels. The maximum number of images is 10,000 images or 100 MB per .zip file. Encode special characters in the file name in UTF-8.
        :param file negative_examples: A .zip file of images that do not depict the visual subject of any of the classes of the new classifier. Must contain a minimum of 10 images. Encode special characters in the file name in UTF-8.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Classifier` response.
        :rtype: dict
        """
        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v3/classifiers/{0}'.format(
            *self._encode_path_vars(classifier_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files=kwargs,
            accept_json=True)
        return response
