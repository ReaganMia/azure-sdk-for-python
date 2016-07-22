# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Dns
  module Models
    #
    # An NS record.
    #
    class NsRecord

      include MsRestAzure

      # @return [String] Gets or sets the name server name for this record,
      # without a terminating dot.
      attr_accessor :nsdname


      #
      # Mapper for NsRecord class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'NsRecord',
          type: {
            name: 'Composite',
            class_name: 'NsRecord',
            model_properties: {
              nsdname: {
                required: false,
                serialized_name: 'nsdname',
                type: {
                  name: 'String'
                }
              }
            }
          }
        }
      end
    end
  end
end