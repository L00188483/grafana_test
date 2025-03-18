

def enable_tracing(f_app):

    # todo, add to requirements.txt: opentelemetry-sdk opentelemetry-instrumentation-fastapi  opentelemetry-exporter-otlp opentelemetry-instrumentation-requests
    #  also launch Tempo in docker

    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    from opentelemetry.trace import set_tracer_provider

    trace_provider = TracerProvider()
    trace_exporter = OTLPSpanExporter(endpoint="http://localhost:4317")  # Change if using another collector
    trace_provider.add_span_processor(BatchSpanProcessor(trace_exporter))

    set_tracer_provider(trace_provider)

    FastAPIInstrumentor.instrument_app(f_app)



'''
REQUEST_COUNTER = Counter(
    "app_requests_total",  # name
    "Total number of requests to the app",  # description
    ["endpoint"],  # Labels (e.g., endpoint name)
)

RANDOM_NUMBER_GAUGE = Gauge(
    "app_random_number",  # name
    "Current value of the random number",  # description
)


@f_app.get("/hello/{name}")
def hello(name: str) -> HelloResponseModel:

    #REQUEST_COUNTER.labels(endpoint="/").inc()
    random_number = random.randint(a=0, b=100)
    #RANDOM_NUMBER_GAUGE.set(random_number)

    return HelloResponseModel(hello=name)

'''
