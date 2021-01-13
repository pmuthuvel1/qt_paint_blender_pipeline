#ifndef BLENDERCLIENT_H
#define BLENDERCLIENT_H
#include <QtCore>
#include <QtNetwork>
#include <QString>

class BlenderClient : public QObject
{
    Q_OBJECT
public:
    explicit BlenderClient(QObject *parent = 0);

public slots:
    bool connectToHost(QString host);
    bool writeData(QByteArray data);

private:
    QTcpSocket *socket;
};

#endif // BLENDERCLIENT_H
