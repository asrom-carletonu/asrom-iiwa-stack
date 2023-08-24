#include <ros/ros.h>
#include <iiwa_msgs/JointVelocity.h>
#include <iiwa_msgs/JointPosition.h>

class VelocityController {
private:
    static constexpr double KP = 0.5;
    static constexpr double KI = 0.000001;
    static constexpr double I_SAT = 1.0;
    static constexpr double MIN_ERROR = -6.0;
    static constexpr double MAX_ERROR = 6.0;
    static constexpr double MAX_ANG_VEL = 2.0;
    static constexpr double PUBLISH_RATE = 10.0;

    ros::NodeHandle nh;
    ros::Publisher pub;
    ros::Subscriber current_position_sub;
    ros::Subscriber goal_position_sub;
    iiwa_msgs::JointVelocity command_velocity;
    iiwa_msgs::JointPosition current_position;
    iiwa_msgs::JointPosition goal_position;
    double integral;

public:
    VelocityController() : nh("~"), integral(0.0) {
        pub = nh.advertise<iiwa_msgs::JointVelocity>("/iiwa/command/JointVelocity", 10);
        current_position_sub = nh.subscribe("/iiwa/state/JointPosition", 10, &VelocityController::currentPositionCallback, this);
        goal_position_sub = nh.subscribe("/iiwa/goal/JointPosition", 10, &VelocityController::goalPositionCallback, this);
    }

    void currentPositionCallback(const iiwa_msgs::JointPosition::ConstPtr &msg) {
        current_position = *msg;
    }

    void goalPositionCallback(const iiwa_msgs::JointPosition::ConstPtr &msg) {
        goal_position = *msg;
    }

    void computeError() {
        if (!std::isnan(goal_position.position.a4) && !std::isnan(current_position.position.a4)) {
            double raw_error = goal_position.position.a4 - current_position.position.a4;
            double norm_error = 2 * (raw_error - MIN_ERROR) / (MAX_ERROR - MIN_ERROR) - 1;
            integral += norm_error;
            command_velocity.velocity.a4 = KP * norm_error + KI * integral;

            // Publish the command velocity
            pub.publish(command_velocity);

            ROS_INFO("Integral: %f | Normalized Error: %f | Command Velocity: %f", integral, norm_error, command_velocity.velocity.a4);
        }
    }

    void run() {
        ros::Rate rate(PUBLISH_RATE);
        while (ros::ok()) {
            computeError();
            ros::spinOnce();
            rate.sleep();
        }
    }
};

int main(int argc, char **argv) {
    ros::init(argc, argv, "VelocityController");
    VelocityController velocityController;
    velocityController.run();
    return 0;
}
