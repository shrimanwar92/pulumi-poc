import sys
sys.path.append('../../')
from lib.crosswalklambda import CxCrosswalkLbLambda
from main import MyComponent

class CxCWDemoComponent(MyComponent):
    def __init__(self, name, **opts):
        super().__init__(self.__class__.__name__, name, opts)

        cw_resporce = CxCrosswalkLbLambda(self)

        self.print_outputs({
            'lb_dns': cw_resporce.lb.load_balancer.dns_name
        })


CxCWDemoComponent('my-cx-cw-demo-component')
