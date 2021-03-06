#include "blenderclient.h"

static inline QByteArray IntToArray(qint32 source);

BlenderClient::BlenderClient(QObject *parent) : QObject(parent)
{
    socket = new QTcpSocket(this);
}

bool BlenderClient::connectToHost(QString host)
{
    socket->connectToHost(host, 5555);
    return socket->waitForConnected();
}

bool BlenderClient::writeData(QByteArray data)
{
    if(socket->state() == QAbstractSocket::ConnectedState)
    {
        socket->write(IntToArray(data.size())); //write size of data
        socket->write(data); //write the data itself
        return socket->waitForBytesWritten();
    }
    else
        return false;
}

QByteArray IntToArray(qint32 source) //Use qint32 to ensure that the number have 4 bytes
{
    //Avoid use of cast, this is the Qt way to serialize objects
    QByteArray temp;
    QDataStream data(&temp, QIODevice::ReadWrite);
    data << source;
    return temp;
}
