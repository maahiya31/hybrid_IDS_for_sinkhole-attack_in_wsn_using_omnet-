package hybrid_intrusion_detection_for_sinkhole_defense.simulations;

import inet.linklayer.ieee80211.mac.contract.ICollisionController;
import inet.networklayer.configurator.ipv4.Ipv4NetworkConfigurator;
import inet.node.base.NodeBase;
import inet.node.bgp.BgpRouter;
import inet.node.inet.Router;
import inet.node.inet.AdhocHost;
import inet.node.inet.StandardHost;
import inet.physicallayer.wireless.ieee80211.packetlevel.Ieee80211ScalarRadioMedium;
import inet.visualizer.base.TreeVisualizerBase;
import ned.DatarateChannel;

network WSN_Network
{
    parameters:
        int numSensors;
        @display("bgb=2500,2500,#FFCF9F,#00D56A,8;i=misc/signal_departure");
    types:
        channel fiberline extends DatarateChannel
        {
            delay = 1us;
            datarate = 512Mbps;
        }
        channel ethline extends DatarateChannel
        {
            delay = 50ns;
            datarate = 100Mbps;
        }
    submodules:
        radioMedium: Ieee80211ScalarRadioMedium {
            parameters:
                @display("p=100,200;is=s");
        }

        server: StandardHost {
            @display("p=795,850;i=device/router,#C891FF;is=vl");
        }
        configurator: Ipv4NetworkConfigurator {
            @display("p=100,100;is=s");
        }
        Sensor_Node[numSensors]: AdhocHost {
            parameters:
                @display("p=483,296;i=misc/sensor;is=n");

        }

        Base_Station_2: NodeBase {
            @display("p=1771,1691;i=abstract/base1,#800000;is=n");
        }
    connections:

}

