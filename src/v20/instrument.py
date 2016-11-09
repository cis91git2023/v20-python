import ujson as json
from v20.base_entity import BaseEntity
from v20.base_entity import EntityDict
from v20.request import Request
from v20 import entity_properties



class Candlestick(BaseEntity):
    """
    The Candlestick representation
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = ""

    #
    # Format string used when generating a name for this object
    #
    _name_format = ""

    #
    # Property metadata for this object
    #
    _properties = entity_properties.instrument_Candlestick

    def __init__(self, **kwargs):
        """
        Create a new Candlestick instance
        """
        super(Candlestick, self).__init__()
 
        #
        # The start time of the candlestick
        #
        self.time = kwargs.get("time")
 
        #
        # The candlestick data based on bids. Only provided if bid-based
        # candles were requested.
        #
        self.bid = kwargs.get("bid")
 
        #
        # The candlestick data based on asks. Only provided if ask-based
        # candles were requested.
        #
        self.ask = kwargs.get("ask")
 
        #
        # The candlestick data based on midpoints. Only provided if midpoint-
        # based candles were requested.
        #
        self.mid = kwargs.get("mid")
 
        #
        # The number of prices created during the time-range represented by the
        # candlestick.
        #
        self.volume = kwargs.get("volume")
 
        #
        # A flag indicating if the candlestick is complete. A complete
        # candlestick is one whose ending time is not in the future.
        #
        self.complete = kwargs.get("complete")

    @staticmethod
    def from_dict(data):
        """
        Instantiate a new Candlestick from a dict (generally from loading a
        JSON response). The data used to instantiate the Candlestick is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        if data.get('bid') is not None:
            data['bid'] = \
                CandlestickData.from_dict(
                    data['bid']
                )

        if data.get('ask') is not None:
            data['ask'] = \
                CandlestickData.from_dict(
                    data['ask']
                )

        if data.get('mid') is not None:
            data['mid'] = \
                CandlestickData.from_dict(
                    data['mid']
                )

        return Candlestick(**data)


class CandlestickData(BaseEntity):
    """
    The Candlestick representation
    """

    #
    # Format string used when generating a summary for this object
    #
    _summary_format = ""

    #
    # Format string used when generating a name for this object
    #
    _name_format = ""

    #
    # Property metadata for this object
    #
    _properties = entity_properties.instrument_CandlestickData

    def __init__(self, **kwargs):
        """
        Create a new CandlestickData instance
        """
        super(CandlestickData, self).__init__()
 
        #
        # The first (open) price in the time-range represented by the
        # candlestick.
        #
        self.o = kwargs.get("o")
 
        #
        # The highest price in the time-range represented by the candlestick.
        #
        self.h = kwargs.get("h")
 
        #
        # The lowest price in the time-range represented by the candlestick.
        #
        self.l = kwargs.get("l")
 
        #
        # The last (closing) price in the time-range represented by the
        # candlestick.
        #
        self.c = kwargs.get("c")

    @staticmethod
    def from_dict(data):
        """
        Instantiate a new CandlestickData from a dict (generally from loading a
        JSON response). The data used to instantiate the CandlestickData is a
        shallow copy of the dict passed in, with any complex child types
        instantiated appropriately.
        """

        data = data.copy()

        return CandlestickData(**data)


class EntitySpec(object):
    """
    The instrument.EntitySpec wraps the instrument module's type definitions 
    and API methods so they can be easily accessed through an instance of a v20
    Context.
    """

    Candlestick = Candlestick
    CandlestickData = CandlestickData

    def __init__(self, ctx):
        self.ctx = ctx


    def candles(
        self,
        instrument,
        **kwargs
    ):
        """
        Fetch candlestick data for an instrument.

        Args:
            instrument:
                Instrument to get candlestick data for
            price:
                The Price component(s) to get candlestick data for. Can contain
                any combination of the characters "M" (midpoint candles) "B"
                (bid candles) and "A" (ask candles).
            granularity:
                The granularity of the candlesticks to fetch
            count:
                The number of candlesticks to return in the reponse. Count
                should not be specified if both the start and end parameters
                are provided, as the time range combined with the graularity
                will determine the number of candlesticks to return.
            fromTime:
                The start of the time range to fetch candlesticks for.
            toTime:
                The end of the time range to fetch candlesticks for.
            smooth:
                A flag that controls whether the candlestick is "smoothed" or
                not.  A smoothed candlestick uses the previous candle's close
                price as its open price, while an unsmoothed candlestick uses
                the first price from its time range as its open price.
            includeFirst:
                A flag that controls whether the candlestick that is covered by
                the from time should be included in the results. This flag
                enables clients to use the timestamp of the last completed
                candlestick received to poll for future candlesticks but avoid
                receiving the previous candlestick repeatedly.
            dailyAlignment:
                The hour of the day (in the specified timezone) to use for
                granularities that have daily alignments.
            alignmentTimezone:
                The timezone to use for the dailyAlignment parameter.
                Candlesticks with daily alignment will be aligned to the
                dailyAlignment hour within the alignmentTimezone.
            weeklyAlignment:
                The day of the week used for granularities that have weekly
                alignment.

        Returns:
            v20.response.Response containing the results from submitting the
            request
        """

        request = Request(
            'GET',
            '/v3/instruments/{instrument}/candles'
        )

        request.set_path_param(
            'instrument',
            instrument
        )

        request.set_param(
            'price',
            kwargs.get('price')
        )

        request.set_param(
            'granularity',
            kwargs.get('granularity')
        )

        request.set_param(
            'count',
            kwargs.get('count')
        )

        request.set_param(
            'from',
            kwargs.get('fromTime')
        )

        request.set_param(
            'to',
            kwargs.get('toTime')
        )

        request.set_param(
            'smooth',
            kwargs.get('smooth')
        )

        request.set_param(
            'includeFirst',
            kwargs.get('includeFirst')
        )

        request.set_param(
            'dailyAlignment',
            kwargs.get('dailyAlignment')
        )

        request.set_param(
            'alignmentTimezone',
            kwargs.get('alignmentTimezone')
        )

        request.set_param(
            'weeklyAlignment',
            kwargs.get('weeklyAlignment')
        )

        response = self.ctx.request(request)


        if response.content_type is None:
            return response

        if not response.content_type.startswith("application/json"):
            return response

        jbody = json.loads(response.raw_body)

        parsed_body = {}

        #
        # Parse responses specific to the request
        #
        if str(response.status) == "200":
            if jbody.get('instrument') is not None:
                parsed_body['instrument'] = \
                    jbody.get('instrument')

            if jbody.get('granularity') is not None:
                parsed_body['granularity'] = \
                    jbody.get('granularity')

            if jbody.get('candles') is not None:
                parsed_body['candles'] = [
                    Candlestick.from_dict(d)
                    for d in jbody.get('candles')
                ]

        #
        # Assume standard error response with errorCode and errorMessage
        #
        else:
            errorCode = jbody.get('errorCode')
            errorMessage = jbody.get('errorMessage')

            if errorCode is not None:
                parsed_body['errorCode'] = errorCode

            if errorMessage is not None:
                parsed_body['errorMessage'] = errorMessage

        response.body = parsed_body

        return response
